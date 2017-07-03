
from os import *
from shutil import *
from math import *


SUITPRIMES = [2, 3, 5, 7]

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
	upperlimit = int(sqrt(n))
	
	for x in xrange(2,upperlimit) :
		if n%x == 0:
			lowfactors.append(x)
	
	if lowfactors == [] :
		return -1
		
	highfactors = [ n/x for x in lowfactors ]	
	
	return [1] + lowfactors + highfactors[::-1] + [n]

def properDivisors(n):
	
	lowfactors = []
	upperlimit = int(sqrt(n))
	
	for x in xrange(2,upperlimit) :
		if n%x == 0:
			lowfactors.append(x)
	
	if lowfactors == [] :
		return [0 , 1]
	
	highfactors = [ n/x for x in lowfactors ]	
	
	return [1] + lowfactors + highfactors[::-1]
	
def checkPalindromic(n):
	strnum = str(n)
	numofdigits = len(strnum)
	
	for x in range(0, numofdigits/2):
		if strnum[x] != strnum[numofdigits - x - 1]:
			# print strnum[0],  strnum[numofdigits - x - 1]
			
			return -1
	print numofdigits		
	return 1

def sumOfDigits(n):
	dummy = str(n)
	sum = 0
	for x in range(0,len(dummy)):
		sum += int(dummy[x])
	
	return sum
	
def hasAmicablePair(n):
	
	possiblepair = 0
	dummy = properDivisors(n)
#	print dummy , "This is DUMMY", sum(dummy)
	if dummy[0] != 0 :
		possiblepair = sum(dummy)
		if properDivisors(possiblepair)[0] != 0 :
			if n == sum(properDivisors(possiblepair)):
				return possiblepair	
	
	return -1
	

	
dummy  = 0 
result = 0 

"""
for x in xrange(10,100):
	print x, properDivisors(x)
	
"""
for x in xrange(10,10000):
	temp = hasAmicablePair(x)
	if temp != -1:
		if temp != x :
			print x, temp
			result += x

print result 