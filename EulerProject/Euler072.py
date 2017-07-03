import time
import sys
import string
from math import *
starttime,sol = time.time(), 0
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

def numberOfProperFractions(n):
	
	
	f = []
	perfectSquare = False
	if isPrime(n) : return n-1
	upperlimit = sqrt(n)
	if upperlimit == int(upperlimit) : 
		return int((n*numberOfProperFractions(upperlimit))/upperlimit)
	
	res = n
	for x in range(2, int(upperlimit) + 1) :
		if n%x == 0 : f.append(x)

	for x in f[::-1] : f.append(n/x) 
	p = [i for i in f if isPrime(i)]
	
	for x in p :
		res *= x-1
		res /= x
	return res

	
def numberOfProperFractionsDetailed(n):
	res = 0 
	kind = ''
	f = []
	perfectSquare = False
	if isPrime(n) : 
		kind = 'Prm'
		res = n-1
	upperlimit = sqrt(n)
	if upperlimit == int(upperlimit) : 
		res = int((n*numberOfProperFractions(upperlimit)[1])/upperlimit)
		kind = 'Sqr'
	
	if kind =='' :
		res = n
		for x in range(2, int(upperlimit) + 1) :
			if n%x == 0 : f.append(x)
	
		for x in f[::-1] : f.append(n/x) 
		p = [i for i in f if isPrime(i)]
		
		for x in p :
			res *= x-1
			res /= x
		kind = 'Nrm'
	return [kind, res]
	
	
step = 1
ulimit =1000000 + 1
llimit =2 
"""
x = 6 
print x, numberOfProperFractions(x)
"""
for x in range(llimit,ulimit):
	if x%10000 == 0 : 
		print '.',
		if x%100000 == 0 : print
	#print x, numberOfProperFractions(x)
	sol += numberOfProperFractions(x)

print "*****************************************************************"	
print "**  Answer   :\t{0}\n**  Found in :\t{1} ".format(sol, time.time() - starttime)
print "*****************************************************************"	
# A 303963552391 T 58.5789999962

