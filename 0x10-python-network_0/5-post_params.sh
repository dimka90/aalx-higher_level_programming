#!/bin/bash
# a bash script that sends key value pairs to the server
curl -sX POST $1 -d "email=test@gmail.com&subject=I will always be here for PLD" -L
