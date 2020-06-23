Wrap a neural network model with Flask  

 # Build docker image
 docker build -t flask_app .
 
 # Run docker
 docker run -p 8080:8080 flask_app serve
 
 # Run tests on docker
 docker exec <container_id> pytest 

 # Url for testing
 https://picsum.photos/200/300
 
