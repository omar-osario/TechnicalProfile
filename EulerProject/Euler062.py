import time 
from math import pow
from collections import Counter
starttime = time.time()
solfound,sol = False, 0

# 1 digit cubes are x**3 where x in [0,3]
# 2 digit cubes are x**3 where x in [3,5]
# 3 digit cubes are x**3 where x in [5,10]
# 4 digit cubes are x**3 where x in [10,22]
# 5 digit cubes are x**3 where x in [22,47]
# 6 digit cubes are x**3 where x in [47,100]
# 7 digit cubes are x**3 where x in [100,216]
# 8 digit cubes are x**3 where x in [216,465]
# 9 digit cubes are x**3 where x in [465,1000]
# 10 digit cubes are x**3 where x in [1000,2155]
# 11 digit cubes are x**3 where x in [2155,4642]
# 12 digit cubes are x**3 where x in [4642,10000]

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
	

cubelist = [i**3 for i in range(405,10000)]
counterlist = []

for x in cubelist:
	dummy = Counter()
	for y in str(x): dummy[y] += 1
	counterlist.append(dummy)
	

	
for a in range(len(counterlist)) :
	#print a,
	if solfound : break 
	for b in range(a+1,len(counterlist)) :
		if not counterlist[a] == counterlist[b] : continue
		for c in range(b+1,len(counterlist)) :
			if not counterlist[a] == counterlist[c] : continue
			for d in range(c+1,len(counterlist)) :
				if not counterlist[a] == counterlist[d] : continue
				for e in range(d+1,len(counterlist)) :
					if not counterlist[a] == counterlist[e] : continue
					sol = cubelist[a]
					solfound = True
	
	
"""
# This method took over two minutes so it was replaced with method above
for a in range(len(cubelist)) :
	if solfound : break 
	for b in range(a+1,len(cubelist)) :
		if not isPermutation(cubelist[a],cubelist[b]) : continue
		for c in range(b+1,len(cubelist)) :
			if not isPermutation(cubelist[b],cubelist[c]) : continue
			for d in range(c+1,len(cubelist)) :
				if not isPermutation(cubelist[c],cubelist[d]) : continue
				for e in range(d+1,len(cubelist)) :
					if not isPermutation(cubelist[d],cubelist[e]) : continue
					sol = cubelist[a]
					solfound = True
"""
							

print "\n*************************************************"	
print "**  Answer   :\t{:>25}      **".format(sol)
print "**  Found in :\t{:>25}      **".format(time.time() - starttime)
print "*************************************************"
# A 127035954683 T 394.148999929
# A 127035954683 T 151.671999931
# A 127035954683 T 146.256000042
# A 127035954683 T 10.0929999352
# A 127035954683 T 8.67999982834
