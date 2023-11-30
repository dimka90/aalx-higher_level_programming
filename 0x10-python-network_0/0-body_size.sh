#!/bin/bash
# This script uses cURL to send a HEAD request to a specified URL,
curl -sI $1 | grep "Content-Length" | cut -d " " -f2
