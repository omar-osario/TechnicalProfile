
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
	
	return -1

def findFactors(n):
	
	lowfactors = []
	highfactors = []
	
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
	
	return [1] + lowfactors + highfactors[::-1] + [n]

	
results = findFactors(600851475143)

for x in results[::-1]:
	if isPrime(int(x)) == -1 :
		print x, " is a prime factor"
	else :
		print x, " is a NOT i repeat NOT a prime factor"
		
print results