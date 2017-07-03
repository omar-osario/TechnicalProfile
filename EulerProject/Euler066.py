import time 
from math import sqrt
from mth import ContFractionSqrt
starttime = time.time()
solfound,sol = False, 0

ulimit = 1000
llimit = 2

def getConvergent(cfrac):
	l = len(cfrac[1])
	r = l - 1
	if r % 2 == 0 : r = 2*r + 1
	
	p = [1, cfrac[0]]
	q = [0, 1]
	
	for x in range(2*r):
		p.append(cfrac[1][x%l]*p[x+1] + p[x]) 
		q.append(cfrac[1][x%l]*q[x+1] + q[x])
	return [p[r+1], q[r+1]]

sol = 0 
dummy = 0 

for x in range(1001):
	d = sqrt(x)
	if int(d) == d : continue

	a,b = getConvergent(ContFractionSqrt(x))
	if a > dummy :
		dummy = a 
		sol = x

		
print "\n*************************************************"	
print "**  Answer   :\t{:>25}      **".format(sol)
print "**  Found in :\t{:>25}      **".format(time.time() - starttime)
print "*************************************************"
# X 66249 T UNKNOWN ( was done while program was running) 
# A 661 T 0.0529999732971 
# A 661 T 0.029000043869