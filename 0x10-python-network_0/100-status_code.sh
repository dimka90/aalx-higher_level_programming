#!/bin/bash
# a bash script that prints the status code of a response body without using redirection
curl -o /dev/null -sw "%{http_code}" $1
