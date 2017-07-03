import time
import sys
import string
from math import sqrt
from collections import Counter
starttime,sol = time.time(), 0
SUITPRIMES = [2,3,5,7]

def isPermutation(n,m):
	tempa, tempb = str(n), str(m)
	if len(tempa) != len(tempb) : return False
	a, b = Counter(), Counter()
	for x in range(len(tempa)):
		a[tempa[x]] += 1
		b[tempb[x]] += 1
	if a == b : return True
	return False

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

def EulerTotient(n):
	f = []
	if isPrime(n) : return int(n-1)
	upperlimit = sqrt(n)
	if upperlimit == int(upperlimit) : 
		return int((n*EulerTotient(upperlimit))/upperlimit)
	
	res = n
	for x in range(2, int(upperlimit) + 1) :
		if n%x == 0 : f.append(x)

	for x in f[::-1] : f.append(n/x) 
	p = [i for i in f if isPrime(i)]
	
	for x in p :
		res *= x-1
		res /= x
	return int(res)

def relativePrime(n):

	if isPrime(n) : return [i for i in range(1,n)]
	
	upperlimit = sqrt(n)
	if upperlimit == int(upperlimit) : 
		return relativePrime(int(upperlimit))
	
	res = n
	f=[]
	for x in range(2, int(upperlimit) + 1) :
		if n%x == 0 : f.append(x)

	for x in f[::-1] : f.append(n/x) 
	p = [i for i in f if isPrime(i)]
	
	return p 
	
	
ulimit = 1*(10**7)
compare = 100
i = 0 

f = open('primesunder10000.txt','r').read().split(',')
primes = [ int(i) for i in f ]



for x in range(0,len(primes)):
	for y in range(x+1,len(primes)):
		arg1 = primes[x]*primes[y]
		if arg1 > ulimit :	break 
		arg2 = (primes[x]-1)*(primes[y]-1)
		if arg2 == 0 : continue
		if float(arg1)/float(arg2) < compare :
			if isPermutation(arg1,arg2):
				compare = float(arg1)/float(arg2)
				sol = arg1



print "*****************************************************************"	
print "**  Answer   :\t{0}\n**  Found in :\t{1} ".format(sol, time.time() - starttime)
print "*****************************************************************"	
# A 8319823 T 833.31099987
# A 8319823 T 772.782000065
# A 8319823 T 58.7509999275
# A 8319823 T 2.3140001297

