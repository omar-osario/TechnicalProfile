import time
from math import sqrt
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

for x in xrange(1,1000000):
	if solfound : break
	for y in [2, 3, 4, 5, 6 ] :
		if not isPermutation(x, x*y): break
		if y == 6:
			sol = x
			solfound = True
			


print "\n*************************************************"	
print "**  Answer   :\t{:>25}      **".format(sol)
print "**  Found in :\t{:>25}      **".format(time.time() - starttime)
print "*************************************************"
# A 142857 T 1.04099988937






