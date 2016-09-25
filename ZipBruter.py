# coding:utf8
import zipfile

# config_start
path = "" # 不指定 path 参数 , 程序从当前目录读取
filename = 'Secret.zip' # 带密码的压缩文件名
dictionaryName = 'Dictionary.txt' # 字典名称
# config_end

filepath = path + filename
zip = zipfile.ZipFile(filepath, "r",zipfile.zlib.DEFLATED)
dictionary = open(dictionaryName)
for line in dictionary:
	password = line[0:-1] # 去掉行尾换行符
	print "Trying : ",
	print password,
	print "...",
	try:
		zip.extractall(members=zip.namelist() , pwd=password) # 不指定 path 参数 , 程序从当前目录读取
		print "Bingo : ",
		print password
		zip.close()
		break
	except:
		print "error!"
		pass
