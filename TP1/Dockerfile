# Utiliser l'image Python officielle comme image de base
FROM python:3.12-slim

# Définir le répertoire de travail à /app
WORKDIR /app

# Copier le code de l'application Flask dans le conteneur
COPY app.py ./

# Installer les dépendances Python
RUN pip install --no-cache-dir Flask

# Exposer le port sur lequel l'application Flask fonctionnera
EXPOSE 3000

# Définir la commande pour exécuter l'application Flask
CMD ["python", "app.py"]