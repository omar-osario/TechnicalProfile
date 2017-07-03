import time
from math import sqrt
starttime,sol = time.time(), 0
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
def findFactors(n):
	
	#if n in SUITPRIMES : [1]
	lowfactors = []
	upperlimit = int(sqrt(n))
	
	for x in xrange(2,upperlimit + 1) :
		if n%x == 0:
			lowfactors.append(x)
	
	if lowfactors == [] :
		return [1]
		
	highfactors = [ n/x for x in lowfactors ]	
	
	return [1] + lowfactors + highfactors[::-1] + [n]

def primeFactors(n):
	lowfactors = []
	upperlimit = int(sqrt(n))
	
	for x in xrange(2,upperlimit+1) :
		if n%x == 0:
			lowfactors.append(x)
	
	if lowfactors == [] :
		return [-1]
		
	highfactors = [ n/x for x in lowfactors ]	
	temp = []
	#print '===*==='
#	print temp
	for x in sorted(lowfactors + highfactors):
		if isPrime(x) : temp.append(x)
#	print temp
	#print '***=***'
	return temp
	
count = 0
for x in range(646, 1000000):
	t = primeFactors(x)
	if len(t) == 4 :
		count += 1
		if count == 4:
			sol = x -3
			break
	else : count = 0 
	

print "\n*************************************************"	
print "**  Answer   :\t{:>25}      **".format(sol)
print "**  Found in :\t{:>25}      **".format(time.time() - starttime)
print "*************************************************"
# A 134043 T 3.8259999752
# A 134043 T 3.74899983406
# A 134043 T  3.42399978638




