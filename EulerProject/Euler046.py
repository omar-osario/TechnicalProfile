import time
from math import sqrt
starttime,sol = time.time(), 0
SUITPRIMES = [2,3,5,7]
def isPrime(n):
	
	if n in SUITPRIMES : return True

	for x in SUITPRIMES :
		if n%x == 0 :
			return False
	
	upperlimit = int(sqrt(n))	
	
	for x in xrange(9,upperlimit +1,2) :
		if n%x == 0:
			return False 

	if n == 1 : return False
	return True



def GoldbachNumber(n):
	ds = 2
	step = 6
	while n - ds > 0:
		if isPrime(n - ds) : return [n-ds, ds]
		ds += step
		step += 4
	return [0,0]
	
def isGoldbachNumber(n):
	ds = 2
	step = 6
	while n - ds > 0:
		if isPrime(n - ds) : return True
		ds += step
		step += 4
	return False
temp = []	
for i in range(9,999999999,2):
	if isPrime(i) : continue
	if not isGoldbachNumber(i) :
		temp.append(i) 
		break
print temp
	
print "\n*************************************************"	
print "**  Answer   :\t{:>25}      **".format(sol)
print "**  Found in :\t{:>25}      **".format(time.time() - starttime)
print "*************************************************"
# W 57 T 0.0160000324249
# W 41 T 0.0620000362396
# W 17 T 0.0940001010895
# A 5777 T 0.153000116348
# A 5777 T 0.148000001907






