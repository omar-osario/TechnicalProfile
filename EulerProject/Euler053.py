
import time
from sets import Set
from math import *
starttime,sol = time.time(), 0

def combinatorics(n,r):
	return factorial(n)/(factorial(r)*factorial(n-r))
		
print combinatorics(5, 3)		

#for x in range(10, 24):
sol = 0

for x in range(0, 101):
	for y in range(1,x):
		if combinatorics(x,y) > 1000000:
			sol += 1
		
	
print "Answer ", sol, "found in", time.time() - starttime
#0.0550000667572