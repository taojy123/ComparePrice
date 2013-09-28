#coding:utf-8

import cookielib
import urllib2
import urllib
import re
import json
import os

cj = cookielib.CookieJar()
opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(cj))
opener.addheaders = [('User-agent', 'Mozilla/5.0 (Windows NT 5.2) AppleWebKit/537.1 (KHTML, like Gecko) Chrome/21.0.1180.89 Safari/537.1'),
                     ('Accept', 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8'),
                     ('Accept-Language', 'zh-cn,zh;q=0.8,en-us;q=0.5,en;q=0.3'),
                     ('Connection', 'keep-alive'),
                     ('Accept-encoding', 'identity')]

def get_page(url, data=None):
    resp = opener.open(url, data)
    page = resp.read()
    return page


if __name__ == "__main__":
    login_page_url = "http://datamirror.csdb.cn/login.htm"
    login_page = get_page(login_page_url)

    formData = urllib.urlencode({"username": "yz_zhao0501@163.com",
                                 "password": "zyz19880516"})
    login_url = "http://auth.csdb.cn/login?service=http%3A%2F%2Fwww.gscloud.cn%2Flogin.jsp%3Ffrom%3Dhttp%253A%252F%252Fwww.gscloud.cn%252F"
    page = get_page(login_url, formData)







