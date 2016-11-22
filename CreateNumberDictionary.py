#!/usr/bin/env python 
# -*- coding: utf-8 -*- 

def createDictionary(length, start, end):
	'''
	功能 : 生成指定长度,指定起始位置,结束位置的数字类型密码字典
	参数 : 
		Length:
			生成的单个密码的长度
		Start:
			起始位置
		End:
			结束位置
	'''
	for i in range(start, end): # 如果需要很大长度的密码字典 , 为了节省内存 , 需要讲range换成xrange
		temp = str(i);
		if len(temp) < length:
			for j in range(length - len(temp)):
				temp = "0" + temp;
		print temp;
		
createDictionary(4,0,10000); # 注意数组从0开始索引
