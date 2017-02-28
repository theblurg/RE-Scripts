#!/usr/bin/python
import re
import collections
import sys

def createString(buffer):
	newBuffer = ""
	for x in buffer:
		newBuffer += x.rstrip('\r\n')

	return newBuffer

def removeConcatination(buffString):
	tmp = re.sub("\\'\\+\\'", '', buffString,0)
	return re.sub('\\"\\+\\"','', tmp, 0)


def removeRedundantCharacter(buffString):
	redundantCharacter = collections.Counter(buffString).most_common(1)[0]
	return re.sub(redundantCharacter[0], '', buffString,0)


def getIOC(buffString):
	obj = re.search('(http\S+)', buffString, 0)
	return obj.group().split('\\')[0].split('\"')[0]



if __name__ == "__main__":
	for x in sys.argv[1:]:
		file = open(x, 'r')
		buffer = file.readlines()
		buffString = createString(buffer)
		buffString = removeConcatination(buffString)
		buffString = removeRedundantCharacter(buffString)
		buffString = getIOC(buffString)
		print buffString
		file.close()
	

