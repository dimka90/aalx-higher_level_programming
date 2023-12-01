#!/usr/bin/python3
"""Fetches and prints the value of  response from a specified."""

import requests
import sys


def get_url(url):
    """
    Args:
         url(str): uniform resource locator
    Fetches the value  of X-Request-Id header vairable from  URL
    entered on the command line
    using request.

    This function sends a GET request to the specified URL,
    retrieves the content,
    and prints information about the response body.

    Returns:
        None
    """
    response = requests.get(url)
    header = response.headers.get("X-Request-Id")

    print("{}".format(header))


if __name__ == "__main__":
    url =  sys.argv[1]
    get_url(url)
