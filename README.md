## quickstart
### install docker && docker-compose
### download code
### download docker image
    docker pull python:3.8
    docker pull nginx:latest
    docket pull redis:latest
### make a python image
    cd hunger/pre-hunger
    sh start.sh
### start
    docker-compose build && docker-compose up -d