# flaskt
## quickstart
### install docker && docker-compose

### download code
    git clone https://github.com/ybones/flaskt.git
### download docker image
    docker pull python:3.8
    docker pull nginx:latest
    docket pull redis:latest
### make a python image
    sh flaskt/pre-flaskt/start.sh
### start
    docker-compose build && docker-compose up -d