#!/usr/bin/python
# coding:utf8
import threading
import zipfile
import time
# config_start
path = "" # 不指定 path 参数 , 程序从当前目录读取
filename = 'Secret.zip' # 带密码的压缩文件名
# config_end

start_time = time.clock()

filepath = path + filename
zip = zipfile.ZipFile(filepath, "r",zipfile.zlib.DEFLATED)

SIGNAL = False

def getStr(number, length):
	'''
	功能 : 数字转成固定长度的字符串

	'''
	password = str(number)
	for i in range(length - len(password)):
		password = "0" + password;
	return password	

def crack(password):
	global SIGNAL
	try:
		# print "Trying : " + password + " ...";
		zip.extractall(members=zip.namelist() , pwd=password) # 不指定 path 参数 , 程序从当前目录读取
		print "The password is : " + password
		zip.close()
		SIGNAL = True
	except:
		pass

def baseCrack(start, end, length):
	'''
	基础解密函数
	'''
	global SIGNAL
	low = start + (int)((end - start) / 2)
	high = low
	while (not SIGNAL):
		# 循环结束条件
		if (start > low) or (end < high):
			break
		crack(getStr(start,length))
		crack(getStr(end,length))
		crack(getStr(low,length))
		crack(getStr(high,length))
		start += 1
		high += 1
		low -= 1
		end -= 1

def quickCrack(length, start, end, times):
	'''
	length:
		密码长度
	start:
		起始密码
	end:
		结束密码
	times:
		密码分组数
	'''
	size = end - start # 用户期望遍历的密码数
	groupNumber = times # 用户期望分组数
	everyLength = (int)(size / groupNumber) # 每组密码的数量

	for i in range(groupNumber):
		sign_start = i * everyLength
		sign_end = (i + 1) * everyLength

		baseCrack(sign_start, sign_end, length)

# 长度 开始标志 结束标志 分组数
quickCrack(4,0,10000, 1)

end_time = time.clock()
print "This crack cost : " + str(end_time - start_time) + " s."
