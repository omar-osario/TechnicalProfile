#Answer is 70600674, acheived not through programming through excell
76588876
from os import *
from shutil import *
from math import *
import time
starttime,sol = time.time(), 0

SUITPRIMES = [2, 3, 5, 7]


def isPrime(n):
	
	for x in SUITPRIMES :
		if n == x :
			return True

	for x in SUITPRIMES :
		if n%x == 0 :
			return False
	
	upperlimit = int(sqrt(n))	
	
	for x in range(9,upperlimit +1,2) :
		if n%x == 0:
			return False 
	else :
		return True

def findFactors(n):
	
	if isPrime(n):
		return [1,n]
	
	lowfactors = []
	highfactors = []
	upperlimit = int(sqrt(n))
					
	for x in range(2,upperlimit) :
		if n % x == 0:
			lowfactors.append(x) 
			highfactors.insert(0,int(n/x))
	
	if ( n % upperlimit == 0 ):
		lowfactors.append(upperlimit)

	return [1] + lowfactors + highfactors + [n]

trianlgenumber = 1
step = 2
found = 0

limit = 500 
while (found == 0) :
	factors = findFactors(trianlgenumber)
	if len(factors) > limit :
		found = 1
		continue
	trianlgenumber += step 
	step += 1


sol = 	trianlgenumber
print ('*'*40)	
print ("**  Answer   :\t{0}\n**  Found in :\t{1} ".format(sol, time.time() - starttime))
print ('*'*40)

# (False,210,0.0936739444732666)
# (False,76588876,8.310395002365112)
