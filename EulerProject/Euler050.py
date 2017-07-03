import time
from math import sqrt
from collections import Counter
starttime, sol, solfound = time.time(), "", False

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

primesums = [[2,1]]
limit = 1000000
base,steps = 5, 2

x = base 

while base < limit:
	if isPrime(x):
		primesums.append([base, steps])
		base += x
		steps += 1
	x += 2

for x in primesums[::-1]:
	if solfound : break
	for y in primesums:
		if x[0] < y[0] : break
		if isPrime(x[0]-y[0]):
			sol = x[0]-y[0]
			solfound = True
			break


print "\n*************************************************"	
print "**  Answer   :\t{:>25}      **".format(sol)
print "**  Found in :\t{:>25}      **".format(time.time() - starttime)
print "*************************************************"
# WA 958577 T 0.112999916077 E 537 3863
# A 997651 T 0.0090000629425





