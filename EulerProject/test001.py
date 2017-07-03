import time
import sys
import string
from math import sqrt
from collections import Counter
from mth import *
starttime,sol = time.time(), 0


def isPermutation(n,m):
	tempa, tempb = str(n), str(m)
	if len(tempa) != len(tempb) : return False
	a, b = Counter(), Counter()
	for x in range(len(tempa)):
		a[tempa[x]] += 1
		b[tempb[x]] += 1
	if a == b : return True
	return False


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


	
#for x in [5, 6, 8, 9 , 121, 122, 123]:
#	print x, numberOfProperFractions(x)
	
ulimit = 100
ratio = 10.0	
#for x in range(ulimit -1 , 1,-1) :
#for x in [5,6,7,8,10,89,16] :
#for x in range(2 ,15) :
#	print x, numberOfRelativePrimes(x)

print contFracRationalApproxFore(1)		
print contFracRationalApproxFore(2)		
print contFracRationalApproxFore(3)		
print contFracRationalApproxFore(4)		



print "*****************************************************************"	
print "**  Answer   :\t{0}\n**  Found in :\t{1} ".format(sol, time.time() - starttime)
print "*****************************************************************"	
# Try 8319823
