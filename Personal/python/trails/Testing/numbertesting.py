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
	if isPrime(n) : return float(n-1)
	upperlimit = sqrt(n)
	if upperlimit == int(upperlimit) : 
		return float((n*EulerTotient(upperlimit))/upperlimit)
	
	res = n
	for x in range(2, int(upperlimit) + 1) :
		if n%x == 0 : f.append(x)

	for x in f[::-1] : f.append(n/x) 
	p = [i for i in f if isPrime(i)]
	
	for x in p :
		res *= x-1
		res /= x
	return float(res)

def relativePrime(n):

	if isPrime(n) : return [i for i in range(1,int(n))]
	
	upperlimit = sqrt(n)
	if upperlimit == int(upperlimit) : 
		return relativePrime(upperlimit)
	
	res = n
	f=[]
	for x in range(2, int(upperlimit) + 1) :
		if n%x == 0 : f.append(x)

	for x in f[::-1] : f.append(n/x) 
	p = [i for i in f if isPrime(i)]
	
	return p 
	
#for x in [5, 6, 8, 9 , 121, 122, 123]:
#	print x, numberOfProperFractions(x)
	
ulimit = 100000
ratio = 10.0	
#for x in range(ulimit -1 , 1,-1) :
for x in range(3 ,ulimit,2) :
	dummy = relativePrime(x)
	#if len(dummy) < 2 or len(dummy) >7: continue 
	if len(dummy) != 3 : continue 
	#if dummy[0] < 10 or dummy[2] < 200 : continue
	#if float(sum(dummy))/float(len(dummy)) == sum(dummy)/len(dummy):
	#	if sum(dummy)/len(dummy) in dummy :
	ratio  = float(x)/EulerTotient(x)
	t = dummy[0]*dummy[1]*dummy[2]
	if t != x :
		print "{:5} {:15} {}".format(x, relativePrime(x), float(x)/EulerTotient(x))
		
			



print "*****************************************************************"	
print "**  Answer   :\t{0}\n**  Found in :\t{1} ".format(sol, time.time() - starttime)
print "*****************************************************************"	

