
import time
from sets import Set
from math import *
starttime,sol = time.time(), 0


pentagonal = lambda n : n*(3*n-1)/2

def isPentagonalNumber_1(n):
	temp = (sqrt(1 + 24*n) + 1.0)/6.0
	return temp == int(temp)

pentagonalarray = [ pentagonal(x) for x in range(1,10000)]

for x in pentagonalarray:
	if sol != 0:
		break 
	for y in range(1,pentagonalarray.index(x)):
		if isPentagonalNumber_1(x - pentagonalarray[y]) and isPentagonalNumber_1(x + pentagonalarray[y]):
			sol = x - pentagonalarray[y]

print "Answer ", sol, "found in", time.time() - starttime
#37.5099999905
#1.58899998665