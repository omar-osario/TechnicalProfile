import time 
from math import sqrt
starttime = time.time()
solfound,sol = False, 0
listofprimes = [3, 7, 109, 673]

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

def hasPrimeProperty(n):
	for x in n :
		for y in n :
			if x == y : continue 
			#print 'testing', (str(x)+str(y))
			if  not isPrime(int(str(x)+str(y))) : return False
	return True		
"""
testprimes = []
f = open('6digitprimes.txt','r')
for l in f:
	testprimes.append(int(l))
"""	
f = open('primesunder1000000.txt','r')
temp = f.read().split(',')
potential = []
print len(temp)
testprimes = [ int(i) for i in temp if int(i)%3 == 1 ]
print len(testprimes)
limit = 10000
for x in range(len(testprimes)):
	if testprimes[x] > limit:
		ulimit = x
		break
print ulimit , testprimes[ulimit]
def sumOfRemarcabePrimes(n):
	print 'testing'
	temp = 0 
	for a in range(len(n)):
		for b in range(a+1,len(n)):
			if  not hasPrimeProperty([n[a], n[b]]): continue
			for c in range(b+1,len(n)):
				if  not hasPrimeProperty([n[a], n[b], n[c]]): continue
				for d in range(c+1,len(n)):
					if  not hasPrimeProperty([n[a], n[b], n[c], n[d]]): continue
					for e in range(d+1,len(n)):
						if hasPrimeProperty([n[a], n[b], n[c], n[d], n[e]]):
							print
							print '=========================================================='
							print n[a], n[b], n[c], n[d], n[e], n[a] + n[b] +  n[c] +  n[d] +  n[e]
							print '=========================================================='
							return n[a] + n[b] +  n[c] +  n[d] +  n[e] 
	#					print '!',
	#				print '@',			
	#			print '#',			
			print '$',			
		print '%',a,'%'			
	return 0 

sol = sumOfRemarcabePrimes(testprimes[:ulimit])

	
print "\n*************************************************"	
print "**  Answer   :\t{:>25}      **".format(sol)
print "**  Found in :\t{:>25}      **".format(time.time() - starttime)
print "*************************************************"
# W 2070064 T 54.126999855
# W 1035037 T 71.5199999809
# W 1035037 T 71.5199999809
# W  848291 T 71.76.1029999256
# A 26033   T 55.126999855
# A 26033   T 11.118999958




