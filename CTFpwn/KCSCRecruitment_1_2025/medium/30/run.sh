#!/bin/sh

docker build . -t m
docker run -it -p 1337:1337 m