
import time
from sets import Set
from math import *
starttime = time.time()

def checkPalindromic(n):
	strnum = str(n)
	numofdigits = len(strnum)
	for x in range(0, numofdigits/2):
		if strnum[x] != strnum[numofdigits - x - 1]:
		
			return -1
	return 1
def checkPalindromicBinary(n):
	
	strnum = str(n)[2::]
	numofdigits = len(strnum)
	
	for x in range(0, numofdigits/2):
		if strnum[x] != strnum[numofdigits - x - 1]:
			return -1
	return 1
	


sum = 0

for x in range(1000000):
	if checkPalindromic(x) == 1 :
		if checkPalindromicBinary(bin(x)) == 1 :
			sum += x
print sum

print "Execution time ", time.time() - starttime
#1.13499999046
#1.09700012207