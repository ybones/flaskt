## quickstart
### install docker && docker-compose
### download code
### download docker image
    docker pull python:3.8
    docker pull nginx:latest
    docket pull redis:latest
### make a web python image
    cd hunger/docker-pre
    sh start.sh
### make a scheduler image
    cd scheduler/docker-pre
    sh start.sh
### start
    docker-compose build && docker-compose up -d