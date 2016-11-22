#!/usr/bin/env python 
# -*- coding: utf-8 -*- 

def getSetOfWords(words):
	'''
	统计出文本中所有有的字符
	'''
	myset = set()
	for ch in words:
		if ch in myset:
			pass
		else:
			myset.add(ch)
	return myset

def getResult(words):
	'''
	返回统计结果(字典)
	'''
	result = {}
	myset = getSetOfWords(words)
	for ch in myset:
		result[ch]=words.count(ch)
	return result

words = input("Please input the words : ")
print getResult(words)
