#!/usr/bin/env bash

docker build --pull -t lappland/pelican Docker
exec docker run -it --rm -v `pwd`:/srv/pelican -p 8000:8000 lappland/pelican
