#!/usr/bin/python3
"""
error code
"""
import requests
import sys
if __name__ == "__main__":
    url = sys.argv[1]
    r = requests.get(url)
    if r.status_code >= 400:
        print("Error code: {}".format(rstatus_code))
    else:
        print(r.text)
