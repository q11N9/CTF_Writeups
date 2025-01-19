#!/bin/sh

docker build . -t yud
docker run -it -p 1337:1337 yud