import time
from mth import *
from gen import *
from math import sqrt
starttime,sol = time.time(), 0
solfound = False

# Google puzzle #4, back in 2008
"""
Find the smallest number that can be expressed as the sum of 7 consecutive prime numbers, the sum of 17 consecutive prime numbers, the sum of 41 consecutive prime numbers, the sum of 541 consecutive prime numbers, and is itself a prime number.

For example, 41 is the smallest prime number that can be expressed as the sum of 3 consecutive primes (11 + 13 + 17 = 41) and the sum of 6 consecutive primes (2 + 3 + 5 + 7 + 11 + 13 = 41).
"""

f = open(base+'primes_0_1000000.txt','r').read().split(',')
primes = [ int(i) for i in f ] 
start = [[7], [17], [41], [541]]
temp_primes = []

for i in start :
	print
	print 'checking', i[0]
	temp = 0 
	for x in range(len(primes)-i[0]):
		if x%4000 == 1333  : print '\b\b/',
		if x%4000 == 2666  : print '\b\b\\',
		if x%4000 == 3999  : print '\b\b-',
		temp = 0
		for a in range(x, x+i[0]) :
			temp+= primes[a]
		if isPrime(temp) :
			i.append(temp)
print
count = 0 
for i in range(len(start[3])) :
	if start[3][i] in start[2] :
		print '.', 
		if start[3][i] in start[1] :
			print '|'
			if start[3][i] in start[0] :
				print start[2][i]
				count += 1
				if count > 20 : break
			
	
	
print '*'*65
print "**  Answer   :\t{0}\n**  Found in :\t{1} ".format(sol, time.time() - starttime)
print '*'*65


