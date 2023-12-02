#!/usr/bin/python3
"""
Sends  request  to a server using a get request.

Usage: python script.py <url>
"""

import sys
import requests


def get_x_request_id(url):
    """
    a function at takes in a URL, sends a request to the URL and displays
    the body of the response (decoded in utf-8).
    Args:
        url (str): The URL to which the request will be sent.

    Returns:
        None
    """
    response = requests.get(url)
    content_type = response.headers.get('X-Request-Id')
    print(content_type)


if __name__ == "__main__":
    try:
        url = sys.argv[1]
        get_x_request_id(url)
    except ValueError:
        print("Usage: python script.py <url>")
