import time
import sys
import string
from math import sqrt
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
	if isPrime(n) : return float(n-1)
	upperlimit = sqrt(n)
	if upperlimit == int(upperlimit) : 
		return float((n*numberOfProperFractions(upperlimit))/upperlimit)
	
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
	
ulimit = 1000000
ratio = 0 	
for x in range(2,ulimit +1):
	if x % 10000 == 0 : 
		print '.',
		if x % 100000 == 0: print 

	if ratio < float(x)/numberOfProperFractions(x): 
		print x , ratio,  float(x)/numberOfProperFractions(x)
		ratio =  float(x)/numberOfProperFractions(x)
		sol = x



print "*****************************************************************"	
print "**  Answer   :\t{0}\n**  Found in :\t{1} ".format(sol, time.time() - starttime)
print "*****************************************************************"	
# X 6 T 42.4210000038
# X 16129 T 60.5309998989
# A 510510 T 60.41300010689