#!/usr/bin/python
# -*- coding:utf-8 -*-

import hashlib
import collections


token = "5cbfb079f15b150122261c8537086d77a"
# 参数示例
params = {
	'amount':'1.00',
	'storeNo':'300014',
	'currency':'USD',
	'merchantNo':'200043',
	'callbackUrl':'https://wx.yuansfer.yunkeguan.com/wx',
	'terminal':'ONLINE',
	'ipnUrl':'https://wx.yuansfer.yunkeguan.com/wx',
	'reference':'seq_1525922323',
	'vendor':'alipay',
	'goodsInfo':'[{"goods_name":"Yuansfer","quantity":"1"}]',
	'timeout':'120'
}

def get_signature(token, params):
    # 参数重排
    order_params = collections.OrderedDict()
    for k in sorted(params):
        order_params[k] = params.get(k)
    # 参数拼接
    params_str_list = []
    for (k, v) in order_params.items():
        params_str_list.append(k+'='+str(v))
    params_str = '&'.join(params_str_list)
    # md5 token
    token_md5 = hashlib.md5()
    token_md5.update(token)
    tk_md5 = token_md5.hexdigest()
    # final str md5
    final_str = params_str + '&' + tk_md5
    final_str_md5 = hashlib.md5()
    final_str_md5.update(final_str)
    return final_str_md5.hexdigest()


print get_signature(token,params)
# b6bfd66531ae7c9499115c7480a2c8aa
