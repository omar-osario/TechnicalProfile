#Answer is 142913828922

from os import *
from shutil import *
from math import *


SUITPRIMES = [2, 3, 5, 7]
primativePythagorean = [[3, 4, 5], [5, 12, 13], [7, 24, 25], [8, 15, 17], [9, 40, 41], [11, 60, 61], [12, 35, 37], [13, 84, 85], [16, 63, 65], [20, 21, 29], [28, 45, 53], [33, 56, 65], [36, 77, 85], [39, 80, 89], [48, 55, 73], [65, 72, 97]]

def isPrime(n):
	
	for x in SUITPRIMES :
		if n == x :
			return -1

	for x in SUITPRIMES :
		if n%x == 0 :
			return x
	
	upperlimit = int(sqrt(n))	
	
	for x in xrange(9,upperlimit +1,2) :
		if n%x == 0:
			return x 
	else :
		return -1

def findFactors(n):
	
	lowfactors = []
	highfactors = []
	print "The number i :", n
	upperlimit = int(sqrt(n))
	
	for x in SUITPRIMES :
		if n%x == 0:
			lowfactors.append(x)
			highfactors.append(n/x)
		
	for x in xrange(9,upperlimit +1,2) :
		if n%x == 0:
			lowfactors.append(x) 
			highfactors.append(n/x)
			
	if lowfactors == [] :
		return -1
	
	return lowfactors + highfactors[::-1]

def checkPalindromic(n):
	strnum = str(n)
	numofdigits = len(strnum)
	
	for x in range(0, numofdigits/2):
		if strnum[x] != strnum[numofdigits - x - 1]:
			# print strnum[0],  strnum[numofdigits - x - 1]
			
			return -1
	print numofdigits		
	return 1


result = sum(SUITPRIMES)

for x in xrange(9, 2000000) :
	if isPrime(x) == -1 :
		result += x
		
print result