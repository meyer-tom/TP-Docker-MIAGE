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

