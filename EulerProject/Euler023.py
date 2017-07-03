"""
Problem 23
02 August 2002

A perfect number is a number for which the sum of its proper divisors is exactly equal to the number. For example, the sum of the proper divisors of 28 would be 1 + 2 + 4 + 7 + 14 = 28, which means that 28 is a perfect number.

A number n is called deficient if the sum of its proper divisors is less than n and it is called abundant if this sum exceeds n.

As 12 is the smallest abundant number, 1 + 2 + 3 + 4 + 6 = 16, the smallest number that can be written as the sum of two abundant numbers is 24. By mathematical analysis, it can be shown that all integers greater than 28123 can be written as the sum of two abundant numbers. However, this upper limit cannot be reduced any further by analysis even though it is known that the greatest number that cannot be expressed as the sum of two abundant numbers is less than this limit.

Find the sum of all the positive integers which cannot be written as the sum of two abundant numbers.
"""

import time
starttime,sol = time.time(), 0
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
	else :
		return -1

def isPerfectNumber(n):
	if n == sum(properDivisors(n)) :
		return True
	return False
	
def deficientAbundantTest(n):
	dummy = sum(properDivisors(n))
	if n > dummy :
		return -1
	if n < dummy :
		return 1
	return 0

def findFactors(n):
	
	lowfactors = []
	upperlimit = int(sqrt(n))
	
	for x in xrange(2,upperlimit) :
		if n%x == 0:
			lowfactors.append(x)
	
	if lowfactors == [] :
		return -1
		
	highfactors = [ n/x for x in lowfactors ]	
	
	return [1] + lowfactors + highfactors[::-1] + [n]

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


	
sol += sum(range(1,28124))

abundantnumbers = [i for i in range (12, 28124) if deficientAbundantTest(i) == 1 ]

for x in range(13,28124) :
	for y in abundantnumbers:
		if x < y +11: break
		if deficientAbundantTest(x-y) == 1 :
			sol -= x
			break
	
print "\n*****************************************************************"	
print "**  Answer   :\t{0}\n**  Found in :\t{1} ".format(sol, time.time() - starttime)
print "*****************************************************************"	
# WA 10757671
# WA 7999356
# WA 3138
# WA 2440395
# WA 391287014
# WA 391286007
# CA 4179871 T 45.2239999771
# CA 4179871 T 36.6599998474

