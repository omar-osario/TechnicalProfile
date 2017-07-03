
from os import *
from shutil import *
from math import *
import time
starttime = time.time()

def checkPalindromic(n):
	strnum = str(n)
	numofdigits = len(strnum)
	
	for x in range(0, int(numofdigits/2)):
		if strnum[x] != strnum[numofdigits - x - 1]:
			return -1

	return 1


found = 0 
largestpalindromic = 0 
	
for x in range(999, 100, -1):
	for y in range(999, 100, -1):
		temp = x*y
		if checkPalindromic(temp) == 1 :
			if largestpalindromic < temp :
				largestpalindromic = temp
				print ("X: ", x, "Y: ", y, "==> result : ", x*y)

print (largestpalindromic)
print ("Execution time ", time.time() - starttime)