#!/usr/bin/env python
# -*- coding: utf-8 -*-
import time
import hmac
import hashlib
import base64
import httplib
import logging
import urllib2
import json
import requests

import httplib, ssl, urllib2, socket

def get_data():
    headers = {
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
    'Accept-Language': 'zh-CN,zh;q=0.8',
    'Connection': 'keep-alive',
    'Host':'www.bitstamp.net',
    'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/28.0.1500.72 Safari/537.36'
    }
    postdata = '{"method": "getMarketDepth", "params": [], "id": 1}'
    conn=httplib.HTTPSConnection("www.bitstamp.net")
    conn.request("GET",'/api/order_book/',None,headers)
    response = conn.getresponse()
    x = response.read()
    open("1.txt","w").write( x )
    return x


if __name__ == "__main__":
    get_data()
