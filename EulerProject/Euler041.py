import time
from math import sqrt
starttime,sol = time.time(), 0
def isPandigital(n, l):
	for x in range(1,l+1):
		if not str(x) in n: return False
	return True
	
def isPrime(n):
	SUITPRIMES = [ 2, 3, 5, 7]
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

for x in range(7654321, 1234566,-1):
	if isPandigital(str(x), 7) and isPrime(x): 
		sol = x
		break

print "\n*************************************************"	
print "**  Answer   :\t{:>25}      **".format(sol)
print "**  Found in :\t{:>25}      **".format(time.time() - starttime)
print "*************************************************"		
# W  7652413 T 0.162999868393 





