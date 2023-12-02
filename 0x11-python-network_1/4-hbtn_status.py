#!/usr/bin/python3
"""
Module: my_requests_module

A simple module for making HTTP GET requests using the requests library.

Usage:
    ./script_name.py

Requirements:
    - requests library

Functions:
    - request_url(url)
"""

import requests


def request_url(url):
    """
    Sends a GET request to the specified URL using the requests library.

    Args:
        url (str): The URL to send the GET request to.

    Returns:
        None

    Prints:
        Body response:
            - type: The data type of the response content.
            - content: The content of the response.
    """
    response = requests.get(url)

    print("Body response:")
    print("\t- type: {}".format(type(response.text)))
    print("\t- content: {}".format(response.text))


if __name__ == "__main__":
    url = "https://alx-intranet.hbtn.io/status"
    request_url(url)
