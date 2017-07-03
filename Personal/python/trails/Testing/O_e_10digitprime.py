import time
import mth
from math import sqrt
# Google puzzle #1, back in 2004 
# { first 10-digit prime found in the consecutive digits of e } .com 

isPrime = mth.isPrime 
e = mth.e
starttime,sol = time.time(), 0
solfound = False

l = 10

for x in range(len(e) - l):
	if isPrime(int(e[x:x+l])):
		sol = e[x:x+l]
		break

print "*****************************************************************"	
print "**  Answer   :\t{0}\n**  Found in :\t{1} ".format(sol, time.time() - starttime)
print "*****************************************************************"	
