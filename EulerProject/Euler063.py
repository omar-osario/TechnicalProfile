import time 
from math import pow
from collections import Counter
starttime = time.time()
solfound,sol = False, 0

def isPermutation(n,m):
	tempa, tempb = str(n), str(m)
	if len(tempa) != len(tempb) : return False
	a, b = Counter(), Counter()
	for x in range(len(tempa)):
		a[tempa[x]] += 1
		b[tempb[x]] += 1
	if a == b : return True
	return False

def isCube(n) :
	temp = pow(n, (1.0/3.0))
	return  len(str(temp).split('.')[1]) == 1

for x in range(1,10):
	for p in range(1,100):
		temp = len(str(x**p))
		if temp < p : break
		if temp == p : sol+= 1



print "\n*************************************************"	
print "**  Answer   :\t{:>25}      **".format(sol)
print "**  Found in :\t{:>25}      **".format(time.time() - starttime)
print "*************************************************"
# A 49 T 1.382999897
# A 49 T 0.00600004196167
# A 49 T 0.00500011444092