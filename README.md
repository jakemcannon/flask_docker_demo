### Simple docker setup for Flask


Running the app
```
docker-compose up --build
```

### Manual Docker commands if compose is not working correctly

Build the image
```
docker build -t flask_docker_demo .
```
Run the container
```
docker run -p 5000:5005 flask_docker_demo
```

