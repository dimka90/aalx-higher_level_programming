#!/usr/bin/python3
"""
Sends  request  to a server using a get request.

Usage: python script.py <url>
"""

import sys
from urllib.request import urlopen, Request
from urllib.error import HTTPError


def success_or_error_code(url):
    """
    a function at takes in a URL, sends a request to the URL and displays
    the body of the response (decoded in utf-8).
    Args:
        url (str): The URL to which the request will be sent.

    Returns:
        None
    """
    req = Request(url)
    try:
        with urlopen(req) as response:
            html = response.read()
            html_str = html.decode('utf-8')
            print(html_str)
    except HTTPError as e:
        # print("Error code: ",e.code)
        print("Error code: {}".format(e.code))
if __name__ == "__main__":
    try:
        url = sys.argv[1]
        success_or_error_code(url)
    except ValueError:
        print("Usage: python script.py <url>")
