#!/bin/bash
docker run --rm -d \
	-v ~/Desktop/projects/nginx/pages:/usr/share/nginx/html \
	-p 8080:80 \
	--name nginx-test \
	nginx
