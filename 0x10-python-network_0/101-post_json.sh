#!/bin/bash
# a bash script that send a json file to server
curl -sX POST -H "Content-type: application/json" -d @$2 $1
