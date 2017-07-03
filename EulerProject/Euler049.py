import time
from math import sqrt
from collections import Counter
starttime,sol = time.time(), ""
SUITPRIMES = [2,3,5,7]
def isPrime(n):
	if n == 1 : return False
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

	
def isPermutation(n,m):
	tempa, tempb = str(n), str(m)
	if len(tempa) != len(tempb) : return False
	a, b = Counter(), Counter()
	for x in range(len(tempa)):
		a[tempa[x]] += 1
		b[tempb[x]] += 1
	if a == b : return True
	return False

tempa, tempx = 0, 0 
solfound = False
primes = [i for i in range(1001,9999) if isPrime(i)]

for x in range(len(primes)-1, 0, -1):
	if solfound : break
	for y in range(x-1, -1, -1):
		if primes[x] == 8147 : break
		if isPermutation(primes[y],primes[x]):
			tempa = primes[x] - primes[y]
			tempx = primes[x] - 2*tempa
			if isPermutation(primes[x], tempx ):
				if tempx in primes:
					sol = str(primes[x]) + str(primes[x]+ tempa) + str(tempx)
					#print str(primes[x]), str(primes[x]+ tempa),  str(tempx)
					
					solfound = True
	


print "\n*************************************************"	
print "**  Answer   :\t{:>25}      **".format(sol)
print "**  Found in :\t{:>25}      **".format(time.time() - starttime)
print "*************************************************"
# A 296962999629 T 5.35299992561
# A 296962999629 T 5.29199981689
# A 296962999629 T 2.3259999752
# A 296962999629 T 2.28399991989
# A 296962999629 T 0.421999931335






