#!/bin/bash

# git clone git@github.com:jacobusa/microservices-backend.git

cd ~/microservices

docker-compose -f ./admin/docker-compose-deploy.yml up -d  --build
docker-compose -f ./main/docker-compose-deploy.yml up -d  --build

