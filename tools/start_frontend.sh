#!/bin/bash
#Useage: ./start_frontend.sh

EXCUTABLE_PATH=../apps/frontend

set -x
cd $EXCUTABLE_PATH
npm run serve
