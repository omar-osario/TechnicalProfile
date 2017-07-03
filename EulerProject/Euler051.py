import time
import string
from math import sqrt
from collections import Counter
starttime = time.time()
solfound, sol = False, ''
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

	
def isPermutation(n,m):
	tempa, tempb = str(n), str(m)
	if len(tempa) != len(tempb) : return False
	a, b = Counter(), Counter()
	for x in range(len(tempa)):
		a[tempa[x]] += 1
		b[tempb[x]] += 1
	if a == b : return True
	return False

numberofdigits = 6
#primes = [i for i in range((10**(numberofdigits-1))+1, 10**(numberofdigits)-1,2) if isPrime(i)]
primes = []
f = open('6digitprimes.txt', 'r')
for line in f:
	primes.append(int(line))

primecounter = Counter()

print 'round 1 *'
for a in range(numberofdigits-1):
	for x in primes :
		temp = str(x)
		primecounter[temp[0:a] + '*' + temp[a+1:]] += 1



print 'round 2 **'
for a in range(numberofdigits-2):
	for x in primes :
		temp = str(x)
		if temp[a] == temp[a+1] :
			primecounter[temp[0:a] + '**' + temp[a+2:]] += 1

print 'round 3 *x*'
for a in range(numberofdigits-3):
	for x in primes :
		temp = str(x)
		if temp[a] == temp[a+2] :
			primecounter[temp[0:a] + '*' +temp[a+1]+ '*'+ temp[a+3:]] += 1

print 'round 4 *xx*'
for a in range(numberofdigits-4):
	for x in primes :
		temp = str(x)
		if temp[a] == temp[a+3] :
			primecounter[temp[0:a] + '*' + temp[a+1:a+3] + '*'+ temp[a+4:]] += 1

print 'round 5 *x*x*'
for a in range(numberofdigits-4):
	for x in primes :
		temp = str(x)
		if temp[a] == temp[a+2] and temp[a] == temp[a+4] :
			primecounter[temp[0:a] + '*' + temp[a+1] + '*'+ temp[a+3] + '*' + temp[a+5:]] += 1
			
dummy = ''
for x in primecounter:
	if  primecounter[x] > 5 :
		print x, primecounter[x]
		if primecounter[x] == 8:
			dummy = x
			break

for x in range(10):
	if isPrime(int(string.replace(dummy, '*', str(x)))) :
		sol = string.replace(dummy, '*', str(x))
		break
	


print "\n*************************************************"	
print "**  Answer   :\t{:>25}      **".format(sol)
print "**  Found in :\t{:>25}      **".format(time.time() - starttime)
print "*************************************************"
# A 121313 T 0.929999828339






