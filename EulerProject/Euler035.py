import time
from sets import Set
from math import *
starttime = time.time()

SUITPRIMES = [2, 3, 5, 7]
NONPRIMES = [0, 1, 4, 6, 8, 9, 12]

def isPrime(n):
	
	for x in NONPRIMES:
		if n == x:
			return 0
	for x in SUITPRIMES :
		if n == x :
			return 1

	for x in SUITPRIMES :
		if n%x == 0 :
			return x
	
	upperlimit = int(sqrt(n))	
	
	for x in xrange(9,upperlimit +1,2) :
		if n%x == 0:
			return x 
	else :
		return 1

def isCircularPrime(n):
	testsum = 0 
	dummy = numberstring = str(n)
	for x in range(len(numberstring)):
		#print "Now checking ", dummy
		if isPrime(int(dummy)) != 1:
		#	print dummy, " is out"
			return 0
		dummy =  dummy[-1] + dummy[0:-1] 
	return 1
	
def hasEvenDigit(n):
	numberstr = str(n)
	for x in numberstr:
		if int(x) % 2 == 0 :
			return 1
	return 0 
	

count = 13
hasEvenDigit(23489072)

for	x in range(101,1000000,2):
	if hasEvenDigit(x) != 1:
		if isCircularPrime(x) == 1 :
			count += 1

print count


print "Execution time ", time.time() - starttime
#5.08599996567
#5.01799988747
#3.83399987221
#1.14499998093