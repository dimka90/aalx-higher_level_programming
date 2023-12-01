#!/usr/bin/python3
"""
Sends an email to a server using a POST request.

Usage: python script.py <url> <email>
"""

import sys
from urllib.request import urlopen, Request
from urllib.parse import urlencode


def send_email_to_server(url, email):
    """
    Sends an email to the specified URL using a POST request.

    Args:
        url (str): The URL to which the POST request will be sent.
        email (str): The email address to be sent in the POST request.

    Returns:
        None
    """
    data = {'email': email}
# URL-encode and encode data for the POST request
    data = urlencode(data)
    data = data.encode('utf-8')

    # Create a POST request
    request = Request(url, data)
    request.method = 'POST'

    with urlopen(request) as response:
        content = response.read()
        print(content.decode('utf-8'))


if __name__ == "__main__":
    try:
        url, email = sys.argv[1:]
        send_email_to_server(url, email)
    except ValueError:
        print("Usage: python script.py <url> <email>")
