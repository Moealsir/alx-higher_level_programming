#!/usr/bin/python3
"""
Script that fetches https://alx-intranet.hbtn.io/status using requests.
"""
import requests


if __name__ == "__main__":
    url = "https://alx-intranet.hbtn.io/status"
    response = requests.get(url)
    content = response.text
    print("Body response:")
    print("    - type:", type(response))
    print("    - content:", content)
