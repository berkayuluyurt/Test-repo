import math
import os
import sys
from urllib import request

import requests

print(sys.version)
print(sys.executable)

print("Berkayyy Hello")

r = requests.get("https://www.coreyms.com")

print(r.status_code)


def a():
    test = "abc"
    return False


name = input("name?")

print("Hello, ", name)
