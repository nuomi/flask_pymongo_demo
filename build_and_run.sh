#!/bin/bash

# STEP1: start a mongo instance first
#docker run --name some-mongo -d mongo


# STEP2: build image from local
echo building...
docker build -t flask-test .

# STEP3: link mongo container and run
sleep 3
echo starting...
docker run --rm --name test -p80:80 --link mongo_test flask-test


