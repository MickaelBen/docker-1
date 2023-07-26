### Build
```Bash
docker build -t test/complex-system .
```

### Get Image Docker
```Bash
docker images
```

### Bind-Mounts
```Bash
docker run -d -v $(pwd)/_data:/usr/src/app/data -p 8080:8080 test/complex-system
docker run -p 80:80 -e MSG_TO_WRITE="from container 1" -v $(pwd)/_data:/opt/demo/data app
docker exec -it a1b987b62d83 bash
```

### Volumes
```Bash
docker volume create vol2
docker volume inspect vol2
docker run -d -v vol2:/usr/src/app/data/ -p 8080:8080 test/complex-system 

#docker volume rm [volume] # Supprimer un volume sur la base de son Id
# docker volume prune # Supprimer les volumes non utilisés
```

### Get container ID
```Bash
docker ps
```

# Enter the container
````Bash
docker exec -it <container id> /bin/bash
docker exec -it 5cdf8712973e /bin/bash
```