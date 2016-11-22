#!/usr/bin/env python 
# -*- coding: utf-8 -*- 

upperDict=['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
lowerDict=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']

def cesarWithLetter(ciphertext,offset):
	'''
	凯撒密码 :
		只转换字母(包括大写小写)
	参数 : 
		ciphertext : 明文
		offset : 偏移量
	'''
	result = ""
	for ch in ciphertext:
		if ch.isupper():
			result=result+upperDict[((upperDict.index(ch)+offset)%26)]
		elif ch.islower():
			result=result+lowerDict[((lowerDict.index(ch)+offset)%26)]
		elif ch.isdigit():
			result=result+ch
		else:
			result=result+ch
	return result

def printAllResult(ciphertext):
	'''
	打印所有偏移结果
	'''
	for i in range(len(upperDict)):
		print cesarWithLetter(ciphertext,i)

ciphertext=input("Please input the words : ")
printAllResult(ciphertext)
