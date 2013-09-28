#!/usr/bin/env python
# -*- coding: utf-8 -*-
import time
import hmac
import hashlib
import base64
import httplib
import logging

import json

import requests

r = requests.get('https://www.bitstamp.net/api/order_book/')


requests.get('https://www.bitstamp.net/api/order_book/')

print 0
conn=httplib.HTTPSConnection("www.bitstamp.net")
print 1
conn.request("POST",'/api/order_book')
print 2
response = conn.getresponse()
print 3
x = response.read()
print x

