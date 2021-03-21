#!/bin/bash

ssh $USER@$MICROIP "source ~/.profile && git clone git@github.com:jacobusa/microservices-backend.git && cd ~/microservices-backend/ && docker-compose -f ./admin/docker-compose-deploy.yml up -d  --build && docker-compose -f ./main/docker-compose-deploy.yml up -d  --build"
# git clone git@github.com:jacobusa/microservices-backend.git

# cd ~/microservices

# git pull origin main

# docker-compose -f ./admin/docker-compose-deploy.yml up -d  --build
# docker-compose -f ./main/docker-compose-deploy.yml up -d  --build

