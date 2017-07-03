import time
from sets import Set
starttime = time.time()

def sumOfNthPower(n, p):
	testsum = 0 
	numberstring = str(n)
	for x in range(len(numberstring)):
		testsum += int(numberstring[x])**p
	if testsum == n :
		return 1
	return -1

upperlimit = 295245	
sum = 0

for	x in range(2,upperlimit):
	if sumOfNthPower(x, 5) == 1:
		print "BAZINGA !!! number is ", x
		sum += x

print sum


print "Execution time ", time.time() - starttime