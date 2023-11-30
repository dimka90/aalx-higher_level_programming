#!/usr/bin/env bash
# This script uses cURL to send a HEAD request to a specified URL,
# extracts the "Content-Length" header from the response, and displays the size in bytes.

# Usage: ./script.sh <URL>
# Example: ./script.sh http://example.com

# Explanation of the command:
# curl -sI $1: Sends a HEAD request to the specified URL ($1) and prints only the headers (-I).
# grep "Content-Length": Filters the output to include only the line containing "Content-Length".
# cut -d " " -f2: Splits the line into fields using space as the delimiter (-d " "),
# and extracts the second field (-f2), which corresponds to the actual content length value.

# Note: The script assumes that the "Content-Length" header is present in the response.
# If the header is not present, the output may be empty.

# Example usage:
# ./script.sh http://example.com
# Output: Content-Length: 12345 (size in bytes)

curl -sI "$1" | grep "Content-Length" | cut -d " " f2
