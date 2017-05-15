#!/bin/bash

BASEDIR=$(pwd)

echo "Running in ${BASEDIR} ..."

stop_server () {
    $BASEDIR/develop_server.sh stop
    trap - INT QUIT TERM EXIT
    exit 0
}

if ! [ -e $BASEDIR/pelicanconf.py ] ; then
    exec pelican-quickstart
fi

if [ "$1" == "publish" ] ; then
    exec make publish
fi

if ! [ -e $BASEDIR/develop_server.sh ] ; then
    exec pelican "$@"
fi

trap stop_server INT QUIT TERM EXIT
$BASEDIR/develop_server.sh start $1

read
