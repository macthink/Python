# coding:utf8
# 遍历所有6位可打印字符的md5字典库 , 将结果打印
import hashlib
md5File = open("md5.txt","a")
#for i in range(1, 100000):
for i in range(33, 127):
	for j in range(33, 127):
		for k in range(33, 127):
			for l in range(33, 127):
				for m in range(33, 127):
					for n in range(33, 127):
						password = chr(i) + chr(j) + chr(k) + chr(l) + chr(m) + chr(n)
						md5Object = hashlib.md5()
						md5Object.update(str(password))
						md5File.write(md5Object.hexdigest() + " " + str(password) + "\n")
						print password
md5File.close()
