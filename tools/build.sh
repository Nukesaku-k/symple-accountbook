#!/bin/bash
#Useage: ./build.sh

EXCUTABLE_PATH=../apps/frontend

set -x
cd $EXCUTABLE_PATH
npm run build
