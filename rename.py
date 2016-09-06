#coding:utf-8
import os
s = os.sep #根据不同的系统决定是/还是\

root = "c:" + s + "Users" + s + "Sun" + s + "Desktop" + s + "python" + s #构建目录

def func(args,dire,fis): #遍历函数
    for file in fis:
        filename = os.path.splitext(file); #分割文件名和后缀名
        print u"发现文件 : ",
        print file;
        if filename[1] == ".bak":
        	print "old name : " + file; #打印旧的文件名
        	newname = filename[0] + ".txt"; #构造新的文件名
        	print "new name : " + newname; #打印新的文件名
        	try:
        		os.rename(os.path.join(dire,file),os.path.join(dire,newname)); #重命名文件
        		#pass
        	except Exception, e:
        		print u"重命名失败 : ",
        		print filename[0] + ".txt",
        		print u"已存在";
        		pass
        		#raise
        	else:
        		pass
        	finally:
        		pass
os.path.walk(root,func,()) #调用函数, 遍历批量重命名