#!/usr/bin/env python 
# -*- coding: utf-8 -*- 

import requests

# config-start
username = "" # 学号
password = "" # 密码
url = "http://www.msftconnecttest.com/srun_portal_pc.php?ac_id=1&"
# config-end

session = requests.Session()
postData = {
        "action":"login",
        "ac_id":"1",
        "user_ip":"",
        "nas_ip":"",
        "user_mac":"",
        "url":"",
        "username":username,
        "password":password,
        "save_me":"1"
        }
response = session.post(url, data=postData)
print response.status_code
print response.text.encode("UTF-8")

# 参考 HTTP 头
# POST /srun_portal_pc.php?ac_id=1& HTTP/1.1
# Host: www.msftconnecttest.com
# Connection: keep-alive
# Cache-Control: max-age=0
# Origin: http://www.msftconnecttest.com
# Upgrade-Insecure-Requests: 1
# User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87 Safari/537.36
# Content-Type: application/x-www-form-urlencoded
# Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8
# Referer: http://www.msftconnecttest.com/srun_portal_pc.php?ac_id=1&
# Accept-Encoding: gzip, deflate
# Accept-Language: zh-CN,zh;q=0.8,en;q=0.6

# 参考 POST 数据
# ac_id:1
# action:login
# ac_id:1
# user_ip:
# nas_ip:
# user_mac:
# url:
# username:
# password:
# save_me:1
