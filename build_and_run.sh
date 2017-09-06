#!/bin/bash

echo building...
docker build -t flask-test .

sleep 3
echo starting...
docker run --rm --name test -p80:80 --link mongo_test flask-test


