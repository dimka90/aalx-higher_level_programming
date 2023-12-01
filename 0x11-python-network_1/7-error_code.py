#!/usr/bin/python3
"""
Sends  request  to a server using a get request.

Usage: python script.py <url>
"""

import sys
import requests


def success_or_error_code(url):
    """
    a function at takes in a URL, sends a request to the URL and displays
    the body of the response (decoded in utf-8).
    Args:
        url (str): The URL to which the request will be sent.

    Returns:
        None
    """
    response = requests.get(url)
    try:
        response.raise_for_status()
        print(response.text)
    except requests.exceptions.HTTPError as err:
    # Print the HTTP error code
        print(f"Error Code: {err.response.status_code}")



if __name__ == "__main__":
    try:
        url = sys.argv[1]
        success_or_error_code(url)
    except ValueError:
        print("Usage: python script.py <url>")

