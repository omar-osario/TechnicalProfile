import time
from sets import Set
from math import factorial
starttime = time.time()

def sumOfDigitFactorial(n):
	testsum = 0 
	numberstring = str(n)
	for x in range(len(numberstring)):
		testsum += factorial(int(numberstring[x]))
	if testsum == n :
		return 1
	return -1

upperlimit = 295245	
sum = 0

for	x in range(3,upperlimit):
	if sumOfDigitFactorial(x) == 1:
		print "BAZINGA !!! number is ", x
		sum += x

print sum


print "Execution time ", time.time() - starttime