#!/bin/bash
app="basic-flask-app"
docker build -t arundocker017/${app} .
docker run -it --rm -v $(pwd):/flask -w /flask -p 5000:5000 arundocker017/${app} $1
