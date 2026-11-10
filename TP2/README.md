# TP2 : Optimisation d'une application Node.js avec Docker

## Mesure initiale

```bash
> docker build --no-cache -t tp2 .
```

Le premier build a duré environ 47 secondes, car l'image `node:latest` devait être téléchargée. Un second build sans cache, avec l'image de base déjà présente sur la machine, a duré environ 20 secondes. Cette seconde mesure sera utilisée comme référence pour la suite.

![Temps du build à froid](images/tps-build-cold-avant-opti.png)

![Temps du build](images/tps-build-avant-opti.png)


La taille de l'image est d'environ 1,88 GB :

![Taille de l'image](images/taille-image-avant-opti.png)



| Version | Temps de build | Taille de l'image |
| --- | ---: | ---: |
| Image initiale | 20 s | 1,88 GB |

## Ajout `.dockerignore` et suppression des node_modules

On ajout `.dockerignore` pour éviter d'envoyer des fichiers inutiles ou sensibles dans le contexte de build :

```dockerignore
node_modules
.git
*.log
.env
.env.*
!.env.example
```

On supprime aussi la ligne qui copie les node_modules dans l'image, car elles ne sont pas nécessaires (elles seront installées directement dans le conteneur) :

```dockerfile
COPY node_modules ./node_modules
```

Après cette modification, le build dure 19 secondes et l'image mesure environ 1,89 GB. Pas grand chose n'a changé par rapport à la version initial. Cette étape permet surtout de rendre le build plus propre, plus sûr et indépendant de la machine locale.

![Temps du build après ajout de .dockerignore](images/tps-build-apres-opti-dockerignore.png)

![Taille de l'image après ajout de .dockerignore](images/taille-image-apres-opti-dockerignore.png)

| Version | Temps de build | Taille de l'image |
| --- | ---: | ---: |
| Image initiale | 20 s | 1,88 GB |
| Avec `.dockerignore` | 19 s | 1,89 GB |

## Optimisation du cache des dépendances

Les fichiers `package.json` et `package-lock.json` sont maintenant copiés avant le reste de l'application :

```dockerfile
COPY package*.json ./
RUN npm ci
COPY . .
```

La commande `npm ci` utilise directement le fichier `package-lock.json`. L'installation est donc reproductible et la couche contenant les dépendances peut être réutilisée tant que les fichiers `package*.json` ne changent pas.

Le build sans cache dure 25,4 secondes. Lorsque les couches sont déjà en cache, il dure 10,5 secondes, soit environ 50% de temps en moins. La taille reste à 1,89 GB, car cette étape optimise le temps de build et non le contenu de l'image finale.

![Temps du build avec cache après optimisation du cache](images/tps-build-sans-cache-apres-opti-cache.png)

![Temps du build avec cache après optimisation du cache](images/tps-build-avec-cache-apres-opti-cache.png)

![Taille de l'image après optimisation du cache](images/taille-image-apres-opti-cache.png)

| Version | Temps de build | Taille de l'image |
| --- | ---: | ---: |
| Image initiale | 20 s | 1,88 GB |
| Avec `.dockerignore` | 19 s | 1,89 GB |
| Cache optimisé, sans cache existant | 25 s | 1,89 GB |
| Cache optimisé, avec cache | 10 s | 1,89 GB |

## Utilisation d'une image de base légère

L'image de base `node:latest` a été remplacée par une image Alpine :

```dockerfile
FROM node:22-alpine
```

Alpine est une distribution Linux beaucoup plus légère qu'une image système complète. La commande qui installait des paquets avec `apt-get` a également été supprimée, car Alpine n'utilise pas ce gestionnaire de paquets et ces dépendances ne sont pas nécessaires à l'application.

Le build sans cache dure 16 secondes et le build avec cache dure 1,9 seconde. La taille de l'image passe de 1,89 GB à 227 MB, soit une réduction d'environ 90%.

![Temps du build avec image Alpine, sans cache](images/tps-build-sans-cache-apres-opti-alpine.png)

![Temps du build avec image Alpine, avec cache](images/tps-build-avec-cache-apres-opti-alpine.png)

![Taille de l'image après optimisation avec image Alpine](images/taille-image-apres-opti-alpine.png)

| Version | Temps de build | Taille de l'image |
| --- | ---: | ---: |
| Image initiale | 20 s | 1,88 GB |
| Avec `.dockerignore` | 19 s | 1,89 GB |
| Cache optimisé, sans cache existant | 25 s | 1,89 GB |
| Cache optimisé, avec cache | 10 s | 1,89 GB |
| Image Alpine, sans cache | 16 s | 227 MB |
| Image Alpine, avec cache | 1,9 s | 227 MB |

## Utilisation d'un multi-stage build

Le Dockerfile a été séparé en deux étapes. La première installe les dépendances et exécute le build :

```dockerfile
FROM node:22-alpine AS build

WORKDIR /app
COPY package*.json ./
RUN npm ci --omit=dev
COPY . .
RUN npm run build
```

La seconde étape crée l'image finale et ne récupère que les éléments nécessaires au fonctionnement de l'application :

```dockerfile
FROM node:22-alpine AS runtime

WORKDIR /app
COPY --from=build /app/node_modules ./node_modules
COPY --from=build /app/server.js ./server.js
CMD ["node", "server.js"]
```

Le build sans cache dure 4,9 secondes et le build avec cache dure 1,5 seconde. La taille obtenue est de 248,2 MB.

![Temps du build avec multi-stage, sans cache](images/tps-build-sans-cache-apres-opti-multi-stage.png)

![Temps du build avec multi-stage, avec cache](images/tps-build-avec-cache-apres-opti-multi-stage.png)

![Taille de l'image après optimisation avec multi-stage](images/taille-image-apres-opti-multi-stage.png)

Dans ce projet, le multi-stage ne réduit pas la taille de l'image : elle augmente même légèrement par rapport aux 227 MB de la version Alpine. Cela s'explique par le fait que l'application est très simple et que son script `build` ne génère pas de véritable dossier `dist`. L'image Alpine précédente était donc déjà très légère. Le multi-stage reste utile pour séparer la préparation de l'application de son image d'exécution, mais il n'apporte pas systématiquement un gain de taille.

| Version | Temps de build | Taille de l'image |
| --- | ---: | ---: |
| Image initiale | 20 s | 1,88 GB |
| Avec `.dockerignore` | 19 s | 1,89 GB |
| Cache optimisé, sans cache existant | 25 s | 1,89 GB |
| Cache optimisé, avec cache | 10 s | 1,89 GB |
| Image Alpine, sans cache | 16 s | 227 MB |
| Image Alpine, avec cache | 1,9 s | 227 MB |
| Multi-stage, sans cache | 4,9 s | 248,2 MB |
| Multi-stage, avec cache | 1,5 s | 248,2 MB |

