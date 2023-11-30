#!/bin/bash
# a bash script that sends key value pairs to the server
curl -sX POST $1 -d "email=test@gmail.com&subject=I%20will%20always%20be%20here%20for%20PLD" -L
