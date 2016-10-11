# coding:utf8
import sys

def cesar(ciphertext):
	'''
	凯撒密码 :
		只转换字母(包括大写小写)
	'''
	result = ""
	for i in range(26):
		for ch in ciphertext:
			if (ord(ch) >= ord('A')) and (ord(ch) <= ord('Z')):
				newch = chr(((ord(ch) - ord('A') + i) % 26) + ord('A'))
			elif (ord(ch) >= ord('a')) and (ord(ch) <= ord('z')):
				newch = chr(((ord(ch) - ord('a') + i) % 26) + ord('a'))
			else:
				newch = ch
			result += newch
			# sys.stdout.write(newch)
		result += "\n"
		# sys.stdout.write("\n");
	return result

ciphertext = "abcdefghijklmnopqrstuvwxyz.1234567890/*-+"

print cesar(ciphertext)
