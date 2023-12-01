#!/usr/bin/python3
"""
Sends an email to a server using a POST request.

Usage: python script.py <url> <email>
"""

import sys
import requests


def send_email_to_server(url, email):
    """
    Sends an email to the specified URL using a POST request.

    Args:
        url (str): The URL to which the POST request will be sent.
        email (str): The email address to be sent in the POST request.

    Returns:
        None
    """

    data = {}
    data["email"] = email
    response = requests.post(url, data=data)

    print(response.text)



if __name__ == "__main__":
    try:
        url, email = sys.argv[1:]
        send_email_to_server(url, email)
    except ValueError:
        print("Usage: python script.py <url> <email>")
