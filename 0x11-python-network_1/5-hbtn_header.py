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
    # Check if the request was successful (status code 200)
    if response.status_code == 200:
        # Retrieve the value of a specific header (e.g., 'Content-Type')
        content_type = response.headers.get('X-Request-Id')
        if content_type:
            print(content_type)
        else:
            print('Content-Type header not present in the response')
    else:
        print(f"Error: {response.status_code}")


if __name__ == "__main__":
    try:
        url = sys.argv[1]
        success_or_error_code(url)
    except ValueError:
        print("Usage: python script.py <url>")
