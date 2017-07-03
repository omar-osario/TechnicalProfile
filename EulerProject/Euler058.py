import time
import sys
import string
from math import sqrt
starttime,sol = time.time(), 0
SUITPRIMES = [2, 3, 5, 7]

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

numbercount, primecount = 1,0
cutoff = 10.00
for x in range(2,1000000,2):
	
	dummy = x**2 +1
	if isPrime(dummy -x) : primecount += 1
	if isPrime(dummy   ) : primecount += 1
	if isPrime(dummy +x) : primecount += 1
	numbercount += 4
	if 100.0*float(primecount)/float(numbercount) < cutoff :
		sol = x + 1
		break

print "*****************************************************************"	
print "**  Answer   :\t{0}\n**  Found in :\t{1} ".format(sol, time.time() - starttime)
print "*****************************************************************"	
#2.30200004578