#!/usr/bin/env python 
# -*- coding: utf-8 -*- 

import requests

# config-start
username = "" # 学号
usertype = "sam" # 用户类型 (职工唯一号 : "hitid") (其他账户 : "")
password = "" # 密码
url = "http://192.168.52.11/cgi-bin/srun_portal"
# config-end

session = requests.Session()
postData = {
        "action":"login",
        "username":username + "@" + usertype,
        "password":password,
        "ac_id":"1",
        "type":"1",
        "wbaredirect":"",
        "mac":"",
        "user_ip":"",
        "vrf_id":"0"
        }
response = session.post(url, data=postData)
print response.status_code
print response.text

# 参考HTTP头
# POST  HTTP/1.1
# Host: 192.168.52.11
# Content-Length: 105
# Origin: http://192.168.52.11/cgi-bin/srun_portal
# User-Agent: Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.99 Safari/537.36
# Content-Type: application/x-www-form-urlencoded
# Accept: */*
# Referer: http://192.168.52.11/srun_portal_pc.php?url=&ac_id=1
# Accept-Encoding: gzip, deflate
# Accept-Language: zh-CN,zh;q=0.8,en;q=0.6
# Cookie: srun_login=11537102
# Connection: close
# 
# action=login&username=*****%40sam&password=&ac_id=1&type=1&wbaredirect=&mac=&user_ip=&vrf_id=0
