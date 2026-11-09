# Exercice : Manipulation de base des conteneurs

1. Vérifiez la version de Docker :

   ```bash
   > docker --version
   Docker version 29.8.2, build 7fc2dff
   ```

2. Listez les images disponibles sur votre machine :

   ```bash
   > docker images
   IMAGE   ID             DISK USAGE   CONTENT SIZE   EXTRA
   ```

3. Téléchargez une image depuis Docker Hub :

   ```bash
   > docker pull hello-world
   Using default tag: latest
   latest: Pulling from library/hello-world
   58dee6a49ef1: Pull complete
   c3bdf82c34d1: Download complete
   Digest: sha256:c567b231f65614688711a75f31518a064258a51d442117a3e771a3a8fdba78ef
   Status: Downloaded newer image for hello-world:latest
   docker.io/library/hello-world:latest
   ```

4. Exécutez un conteneur à partir de l'image :

   ```bash
   > docker run hello-world
   Hello from Docker!
   This message shows that your installation appears to be working correctly.
   ...
   ```

5. Listez les conteneurs en cours d'exécution :

   ```bash
   > docker ps
   CONTAINER ID   IMAGE     COMMAND   CREATED   STATUS    PORTS     NAMES
   ```

6. Listez tous les conteneurs (actifs et stoppés) :

   ```bash
   > docker ps -a
   CONTAINER ID   IMAGE         COMMAND    CREATED         STATUS                     PORTS     NAMES
   6cdc713d12e1   hello-world   "/hello"   3 minutes ago   Exited (0) 3 minutes ago             elated_hopper
   ```

7. Supprimez un conteneur :

   ```bash
   > docker rm 6cdc713d12e1
   6cdc713d12e1
   ```

8. Supprimez une image :

   ```bash
   > docker rmi c567b231f656
   Untagged: hello-world:latest
   Deleted: sha256:c567b231f65614688711a75f31518a064258a51d442117a3e771a3a8fdba78ef
   ```

# Exercice : Création d'un serveur web avec Docker

1. Téléchargez l'image officielle Nginx :

   ```bash
   > docker pull nginx
   Using default tag: latest
   latest: Pulling from library/nginx
   1f7e08c0f6ab: Pull complete
   998fb033610b: Pull complete
   3559a01b6a80: Pull complete
   c64233207369: Pull complete
   34a564bc5d28: Pull complete
   acd43e9bebc3: Pull complete
   c19b54656735: Pull complete
   61b74d3d884f: Download complete
   986a63116111: Download complete
   Digest: sha256:165ddde8751e75a1c907d24ef10d9f6deb08b57e0fe56caf67512486aff76d82
   Status: Downloaded newer image for nginx:latest
   docker.io/library/nginx:latest
   ```

2. Lancez un conteneur Nginx en arrière-plan :

   ```bash
   > docker run -d -p 8080:80 --name mon_nginx nginx
   b4ff42c1150273a96882b8d7d9d9d0f5f4aada3e70d79632dba920032eb2077c
   ```

3. Vérifiez que le conteneur est actif :

   ```bash
   > docker ps
   CONTAINER ID   IMAGE     COMMAND                  CREATED          STATUS          PORTS                                     NAMES
   b4ff42c11502   nginx     "/docker-entrypoint.…"   45 seconds ago   Up 45 seconds   0.0.0.0:8080->80/tcp, [::]:8080->80/tcp   mon_nginx
   ```

4. Accédez à la page dans votre navigateur pour voir la page par défaut de Nginx.
   [http://localhost:8080](http://localhost:8080)
   ![résultat 4.4](images/resultat-4_4.png)

5. Arrêtez le conteneur :

   ```bash
   > docker stop mon_nginx
   mon_nginx
   ```

6. Supprimez le conteneur :

   ```bash
   > docker rm mon_nginx
   mon_nginx
   ```
