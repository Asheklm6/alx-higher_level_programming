#!/usr/bin/python3
"""takes in a URL and an email, sends a
POST request to the passed URL with the email
as a parameter, and displays
the body of the response (decoded in utf-8)"""

from urllib.request import urlopen, Request
import sys
from urllib.parse import urlencode


if __name__ == '__main__':
    url = sys.argv[1]
    email = {
        'email': sys.argv[2]
    }
    email = urlencode(email)
    email = email.encode('ascii')
    request = Request(url, email)
    with urlopen(request) as response:
        string = response.read().decode('utf-8')
        print(string)
