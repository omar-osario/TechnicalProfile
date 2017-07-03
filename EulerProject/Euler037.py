
import time
from sets import Set
from math import *
starttime = time.time()

SUITPRIMES = [ 2, 3, 5, 7]

def isPrime(n):
	
	if n == 1:
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
		
def PrimeTruncatable(n):
	
	numberstr = str(n)
	length = len(numberstr)
	#check from left
	for x in range(length):
	#	print numberstr[0:length-x]
		if isPrime(int(numberstr[0:length-x])) != 1:
			return -1
	#check from left
	for x in range(length):
	#	print numberstr[x:length]
		if isPrime(int(numberstr[x:length])) != 1:
			return -1
	return 1
def hasEvenDigit(n):
	#not first or last digit 
	numberstr = str(n)
	for x in numberstr[1:-1]:
		if int(x) % 2 == 0 :
			return 1
	return -1

sum = 0
numofsol = 0 
#result = []

for x in xrange(11, 1000000001):
	if hasEvenDigit(x) == 1:
		continue
	if PrimeTruncatable(x) == 1 :
		sum += x
		numofsol += 1
	#	result.append(x)
	#	print x, len(result)
		if numofsol == 11:
			break 

#print "the results is "
#print result
print "The sum is :", sum

	
print "Execution time", time.time() - starttime
#4.92499995232
#1.62399983406
#1.61000013351