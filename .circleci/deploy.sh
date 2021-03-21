#!/bin/bash

# ssh $USER@$MICROIP "git clone git@github.com:jacobusa/microservices-backend.git && cd ~/microservices-backend/ && docker-compose -f ./admin/docker-compose-deploy.yml up -d  --build && docker-compose -f ./main/docker-compose-deploy.yml up -d  --build"
ssh $USER@$MICROIP "echo $USER && echo $ADMIN_MYSQL_PASSWORD && echo $MAIN_DEBUG"
# git clone git@github.com:jacobusa/microservices-backend.git

# cd ~/microservices

# git pull origin main

# docker-compose -f ./admin/docker-compose-deploy.yml up -d  --build
# docker-compose -f ./main/docker-compose-deploy.yml up -d  --build

