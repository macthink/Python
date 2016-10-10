# coding:utf8

import requests

dictionary = ['.bak','.back','~','.sql','.temp','.tmp','s'] # 字典 , 扫描的结果和字典相关

url = "" # 输入需要扫描的网站的域名 , 例如 : http://www.baidu.com

fileName = "" # 需要扫描的文件的文件名 , 例如 : index.php

s = requests.Session()

for dic in dictionary:
	newUrl = url + fileName + dic
	response = s.get(newUrl)
	print "Checking : " + newUrl + "\t" + str(response.status_code) + "\t",
	if response.status_code == 200:
		print "OK!"
	else:
		print ""
