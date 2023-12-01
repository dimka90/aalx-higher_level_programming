#!/usr/bin/python3
"""Fetches and prints the body response from a specified URL using urllib."""

from urllib.request import urlopen


def get_url(url):
    """
    Fetches the content of the URL 'https://alx-intranet.hbtn.io/status
    using urllib.

    This function sends a GET request to the specified URL,
    retrieves the content,
    and prints information about the response body.

    Returns:
        None
    """
    with urlopen(url) as response:
        content = response.read()
        print("Body response:")
        print("\t- type:", type(content))
        print("\t- content:", content)
        print("\t- utf8 content:", content.decode('utf-8'))


if __name__ == "__main__":
    url = "https://alx-intranet.hbtn.io/status"
    get_url(url)
