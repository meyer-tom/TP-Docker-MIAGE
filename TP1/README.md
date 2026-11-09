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