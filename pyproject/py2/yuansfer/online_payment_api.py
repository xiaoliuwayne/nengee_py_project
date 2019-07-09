#!/usr/bin/python
# -*- coding:utf-8 -*-

# python2.7

import requests
import json

url = 'https://mapi.yuansfer.com/appTransaction/v2/securepay'

goodsInfo = {
"goods_name":"Yuansfer",
"quantity":"1"
}

verifySign = 'b6bfd66531ae7c9499115c7480a2c8aa'

data = {
	    'merchantNo':   "200043", # customer The merchant NO.
        'storeNo':      "300014",
        'currency':     "USD",
        'amount':       "0.01",
        'vendor':       "wechatpay",
        'reference':    "test201807010121212", # sequence number of customer system
        'ipnUrl':       "https://customer-ipn",        #i nternet accessible 
        'callbackUrl':  "https://customer-callback",   # internet accessible 
        'description':  "description",
        'note':         "note",
        'terminal':     "ONLINE",
        'timeout':      "120",
        'goodsInfo':    json.dumps(goodsInfo),
        'verifySign':   verifySign
}


headers = {
	
}


res = requests.post(
	url=url,
	data=data,
	# headers=headers
	)
print res.text