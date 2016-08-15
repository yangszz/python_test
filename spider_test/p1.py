#! /usr/bin/env python
# -*- coding: utf-8 -*-

import urllib  
import urllib2  

url = 'https://www.zhihu.com'
user_agent = 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.94 Safari/537.36' 
values = {'username' : '15111111111',  'password' : 'ys222222' } 
data = urllib.urlencode(values)
headers = { 'User-Agent' : user_agent}  
request = urllib2.Request(url, headers = headers)  
response = urllib2.urlopen(request)  
page = response.read()
print page
