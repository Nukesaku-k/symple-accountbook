#!/bin/bash
#Useage: (./build.sh)
#Useage: ./start_backend.sh

EXCUTABLE_PATH=../apps/backend

set -x
cd $EXCUTABLE_PATH
pipenv run start
