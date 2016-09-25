# coding:utf8
def creatDictionary(length, start, end):
	'''
		Length:
			生成的单个密码的长度
		Start:
			起始数字
		End:
			结束数字
	'''
	for i in range(start, end): # 如果需要很大长度的密码字典 , 为了节省内存 , 需要讲range换成xrange
		temp = str(i);
		if len(temp) < length:
			for j in range(length - len(temp)):
				temp = "0" + temp;
		print temp;
		
creatDictionary(4,0,10000); # 注意数组从0开始索引
