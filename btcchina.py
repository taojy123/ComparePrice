#!/usr/bin/env python
# -*- coding: utf-8 -*-
import time
import hmac
import hashlib
import base64
import httplib
import logging

import json


# 在这类设置您的个人 API 访问密匙和秘密密匙
access_key="5d320a6c-4a3b-45e4-b6f5-49c2695de6ee"
secret_key="8b9530eb-6a4f-4fcb-9097-341a56c191b7"

tonce=str(int(time.time()*1000000))
params='tonce='+tonce+'&accesskey='+access_key+'&requestmethod=post&id=1&method=getMarketDepth&params='
params_hash = hmac.new(secret_key, params, hashlib.sha1).hexdigest()
base64string = base64.b64encode(access_key+':'+params_hash)
headers = {
'Content-type': 'application/json-rpc',
'Authorization': 'Basic '+base64string,
'Json-Rpc-Tonce': tonce
}
postdata = '{"method": "getMarketDepth", "params": [], "id": 1}'
conn=httplib.HTTPSConnection("api.btcchina.com")
conn.request("POST",'/api_trade_v1.php',postdata,headers)
response = conn.getresponse()

x = response.read()
open("1.txt","w").write( x )
y = json.loads(x)


#format = json.dumps(y['result'],indent=1,separators=(',',':'),sort_keys=True)
dict.update(y['result'])
print y['result']
open("2.txt","w").write( y['result'] )

#print y['result']

#print y.keys()

#print y.items()
