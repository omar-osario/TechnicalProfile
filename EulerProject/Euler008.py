
from os import *
from shutil import *
from math import *


SUITPRIMES = [2, 3, 5, 7]

def isPrime(n):
	
	for x in SUITPRIMES :
		if n == x :
			return -1

	for x in SUITPRIMES :
		if n%x == 0 :
			return x
	
	upperlimit = int(sqrt(n))	
	
	for x in xrange(9,upperlimit +1,2) :
		if n%x == 0:
			return x 
	else :
		return -1

def findFactors(n):
	
	lowfactors = []
	highfactors = []
	print "The number i :", n
	upperlimit = int(sqrt(n))
	
	for x in SUITPRIMES :
		if n%x == 0:
			lowfactors.append(x)
			highfactors.append(n/x)
		
	for x in xrange(9,upperlimit +1,2) :
		if n%x == 0:
			lowfactors.append(x) 
			highfactors.append(n/x)
			
	if lowfactors == [] :
		return -1
	
	return lowfactors + highfactors[::-1]

def checkPalindromic(n):
	strnum = str(n)
	numofdigits = len(strnum)
	
	for x in range(0, numofdigits/2):
		if strnum[x] != strnum[numofdigits - x - 1]:
			# print strnum[0],  strnum[numofdigits - x - 1]
			
			return -1
	print numofdigits		
	return 1

	# done using a calculater no programming needed
	# answer is 40824

teststr = "7316717653133062491922511967442657474235534919493496983520312774506326239578318016984801869478851843858615607891129494954595017379583319528532088055111254069874715852386305071569329096329522744304355766896648950445244523161731856403098711121722383113622298934233803081353362766142828064444866452387493035890729629049156044077239071381051585930796086670172427121883998797908792274921901699720888093776657273330010533678812202354218097512545405947522435258490771167055601360483958644670632441572215539753697817977846174064955149290862569321978468622482839722413756570560574902614079729686524145351004748216637048440319989000889524345065854122758866688116427171479924442928230863465674813919123162824586178664583591245665294765456828489128831426076900422421902267105562632111110937054421750694165896040807198403850962455444362981230987879927244284909188845801561660979191338754992005240636899125607176060588611646710940507754100225698315520005593572972571636269561882670428252483600823257530420752963450"

indexzero = []
indexone = []
skipindex = []
"""
for x in range(0,len(teststr)):
	if int(teststr[x]) == 0:
		indexzero.append(x)
	if int(teststr[x]) == 1:
		indexone.append(x)
	
skipindex = sorted(indexzero + indexone)
"""

skipflag = 0 
largestproduct = 0
dummy = 1
#for x in range(0,50):
for x in range(0,len(teststr)-4):
	if teststr[x] == '0' or teststr[x] == '1' or teststr[x] == '2' or teststr[x] == '3':
		continue 
		
	for y in range(0,5):
		print teststr[x+y],
		dummy *= int(teststr[x+y])
	print dummy
	if 	largestproduct < dummy : 
		largestproduct = dummy
	dummy = 1
	
print largestproduct
	


