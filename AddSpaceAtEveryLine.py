#!/usr/bin/env python
# encoding:utf8

import sys

if len(sys.argv) != 2:
	print "Usage : \r\n\tpython " + sys.argv[0] + " README.md"
	exit(1)
fileName = sys.argv[1] # 文件名
file = open(fileName, "r")
lines = file.readlines() # 一次性将文件全部读进内存
number = len(lines); # 获取行数
for i in range(0, number):
	if lines[i].endswith("  \r\n"):
		continue
	elif lines[i].endswith(" \r\n"):
		lines[i] = lines[i][:-2] + "  \r\n"
	elif lines[i].endswith("\n"):
		lines[i] = lines[i][:-1] + "  \r\n"
	else:
		lines[i] += "  \r\n" # 处理文件结尾
file.close()

# 将文件内容的列表写入文件
file = open(fileName, "w")
for i in range(0, number):
	file.write(lines[i])
file.close()
