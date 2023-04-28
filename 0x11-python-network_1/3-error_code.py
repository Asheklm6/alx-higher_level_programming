#!/usr/bin/python3
"""takes in a URL, sends a request to the URL and
displays the body of the response (decoded in utf-8).
"""

from urllib.request import urlopen, Request
from urllib.error import URLError, HTTPError
from sys import argv


if __name__ == '__main__':
    url = argv[1]

    try:
        with urlopen(url) as response:
            print(response.read().decode('utf-8'))
    except HTTPError as e:
        print('Error code: {}'.format(e.code))
