#!/bin/bash

docker build -t dagit-test .
docker tag dagit-test:latest dagit-test:staging