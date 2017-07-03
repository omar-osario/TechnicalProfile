
import time
from sets import Set
from math import *
starttime,sol = time.time(), 0


triangular = lambda n : n*(n+1)/2
pentagonal = lambda n : n*(3*n-1)/2
hexagonal  = lambda n : n*(2*n-1)

def isTriangularNumber(n):
	temp = (sqrt(1 + 8*n) - 1.0)/2.0
	return temp == int(temp)

def isPentagonalNumber(n):
	temp = (sqrt(1 + 24*n) + 1.0)/6.0
	return temp == int(temp)

def isHexagonNumber(n):
	temp = (sqrt(1 + 8*n) + 1.0)/4.0
	return temp == int(temp)

start = int((sqrt(1 + 8*40755) + 1.0)/4.0) + 1

temparray = [hexagonal(x) for x in range(start , start + 1000000)]

for x in temparray:
	if isHexagonNumber(x) and isPentagonalNumber(x):
			sol = x
			break

print "Answer ", sol, "found in", time.time() - starttime
#0.47100019455
#0.434000015259