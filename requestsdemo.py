#!/usr/bin/env python

# encoding: utf-8

'''

@author: gaoyongxian666

@license: (C) Copyright 2017-2018, Node Supply Chain Manager Corporation Limited.

@contact: deamoncao100@gmail.com

@software: garner

@file: requestsdemo.py

@time: 2018/4/9 21:46

@desc:

'''
import requests



# 带参的request请求
{
  "args": {
    "age": "22",
    "name": "germey"
  },
  "headers": {
    "Accept": "*/*",
    "Accept-Encoding": "gzip, deflate",
    "Connection": "close",
    "Host": "httpbin.org",
    "User-Agent": "python-requests/2.18.4"
  },
  "origin": "121.193.204.10",
  "url": "http://httpbin.org/get?name=germey&age=22"
}

data = {
    'name': 'germey',
    'age': 22
}
headers = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/52.0.2743.116 Safari/537.36'
}
response = requests.get("http://httpbin.org/get", params=data,headers=headers)
print(response.text)

import requests
import json
# 解析json
# 就是把json变成字符串
# 返回的是字符串，可以直接写文件的
response = requests.get("http://httpbin.org/get")
print(type(response.text))
print(response.json())
print(json.loads(response.text))
print(type(response.json()))



# 获取二进制数据
response = requests.get("https://github.com/favicon.ico")
with open('favicon.ico', 'wb') as f:
    f.write(response.content)
    f.close()


# post请求
data = {'name': 'germey', 'age': '22'}
headers = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/52.0.2743.116 Safari/537.36'
}
response = requests.post("http://httpbin.org/post", data=data, headers=headers)
print(response.json())


# response属性
response = requests.get('http://www.jianshu.com')
print(type(response.status_code), response.status_code)
print(type(response.headers), response.headers)
print(type(response.cookies), response.cookies)
print(type(response.url), response.url)
print(type(response.history), response.history)



# 文件上传
files = {'file': open('favicon.ico', 'rb')}
response = requests.post("http://httpbin.org/post", files=files)
print(response.text)

# 获取cookie
response = requests.get("https://www.baidu.com")
print(response.cookies)
for key, value in response.cookies.items():
    print(key + '=' + value)


# cookie会自动处理
s = requests.Session()
s.get('http://httpbin.org/cookies/set/number/123456789')
response = s.get('http://httpbin.org/cookies')
print(response.text)

#证书
# 当我们爬取https的时候，会验证证书，不是官方，返回的数据是提示信息
import requests
from requests.packages import urllib3
# 加上这句就不会报警告
urllib3.disable_warnings()
# 下面这句只是单纯忽略警告
response = requests.get('https://www.12306.cn', verify=False)
print(response.status_code)


# 超时设置
response = requests.get("http://httpbin.org/get", timeout=0.5)

# 设置代理
import requests

proxies = {
    "http": "http://user:password@127.0.0.1:9743/",
}
response = requests.get("https://www.taobao.com", proxies=proxies)
print(response.status_code)