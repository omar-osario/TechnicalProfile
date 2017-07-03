"""
Euler published the remarkable quadratic formula:

n^2 + n + 41

It turns out that the formula will produce 40 primes for the consecutive values n = 0 to 39. However, when n = 40, 402 + 40 + 41 = 40(40 + 1) + 41 is divisible by 41, and certainly when n = 41, 41^2 + 41 + 41 is clearly divisible by 41.

Using computers, the incredible formula  n^2  79n + 1601 was discovered, which produces 80 primes for the consecutive values n = 0 to 79. The product of the coefficients, 79 and 1601, is 126479.

Considering quadratics of the form:

n^2 + an + b, where |a|  1000 and |b|  1000


where |n| is the modulus/absolute value of n
e.g. |11| = 11 and |4| = 4
Find the product of the coefficients, a and b, for the quadratic expression that produces the maximum number of primes for consecutive values of n, starting with n = 0.
"""

from math import *
from decimal import *
import time
starttime,sol = time.time(), 0
SUITPRIMES = [2, 3, 5, 7]
def properDivisors(n):
#does not work for numbers less than 10	

	lowfactors = []
	upperlimit = int(sqrt(n))
	  
	for x in xrange(2,upperlimit+1) :
		if n%x == 0:
			lowfactors.append(x)
	
	if lowfactors == [] :
		return [0 , 1]
	
	if upperlimit**2 == n :
		highfactors = [ n/x for x in lowfactors[:-1] ]	
	else :	
		highfactors = [ n/x for x in lowfactors ]	
	
	return [1] + lowfactors + highfactors[::-1]

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
	else :
		return -1

def howManyPrimes(n,m):
	nonprimefound = True
	x = 0 ;
	while nonprimefound == True :
		temp = x**2 + n*x + m
		if temp < 0 : break
		if not isPrime(temp) == -1 : nonprimefound = False
		else : x+=1
	return x
	
#tempa = tempb = 0
mostprimes = 0
prod = []
for x in range(-1000,0):
	for y in range(0,1001):
		if x < 0 and y < 0 : continue
		temp = howManyPrimes(x,y)
		if temp > mostprimes:
			#tempa = x
			#tempb = y
			prod = [x, y]
			mostprimes = temp
print prod[0], prod[1] , mostprimes
sol = prod[0]*prod[1]
print "\n*****************************************************************"	
print "**  Answer   :\t{0}\n**  Found in :\t{1} ".format(sol, time.time() - starttime)
print "*****************************************************************"	
# CA -59231 T 5.53800010681
# CA -59231 T 4.3220000267
# CA -59231 T 1.77900004387



