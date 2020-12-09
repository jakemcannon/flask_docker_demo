### Simple docker setup for Flask


Running the app
```
docker-compose up
```


### Debugging

When I manually build an image and run it without `docker-compose` my code changes update and I have all these new images. So it appears something with docker-compose and the `docker-compose up --build` is not working correctly. With docker compose there is no new images being created; it seems to just use the very first one.


Build the image
```
docker build -t flask_docker_demo .
```
Run the container
```
docker run -p 5000:5005 flask_docker_demo
```

