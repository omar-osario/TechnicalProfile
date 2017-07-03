
from os import *
from shutil import *
from math import *
import datetime
import time
import calendar

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


startdate = datetime.date(1901, 1, 6)
tempdate = startdate
#tempdate = datetime.date(1999, 12, 6)
enddate = datetime.date(2001, 1, 1)
difference = datetime.timedelta(days=7)
sum = 0
while tempdate < enddate:
	if tempdate.day == 1:	
		sum += 1
	tempdate += difference
	 
print sum
print calendar.SUNDAY