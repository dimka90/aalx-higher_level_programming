#!/bin/bash
# ascript that searches for a particular word from the server and prints it out
curl -o /dev/null -sw "You got me!" 0.0.0.0:5000/catch_me
