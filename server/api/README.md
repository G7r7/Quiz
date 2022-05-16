# Build image

Go to api folder
Execute command 
```sh
docker build -t api_quiz:latest .
```

# Run api
```sh
docker run -it --name api_server_test -p 80:8000 api_quiz:latest
```