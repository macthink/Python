# coding:utf8

def charCounter(words, char):
	counter = 0
	for ch in words:
		if char == ch:
			counter += 1
		else:
			pass
	return counter

def getSetOfWords(words):
	myset = set()
	for ch in words:
		if ch in myset:
			pass
		else:
			myset.add(ch)
	return myset

def printResult(words):
	myset = getSetOfWords(words)
	for ch in myset:
		print ch + " " + str(charCounter(words, ch))

words = "I never said I was the best in all the land, but I will never admit that I was the second."
print words
printResult(words)
