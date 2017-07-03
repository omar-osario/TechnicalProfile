import time
from mth import *
from gen import *
from math import sqrt
starttime,sol = time.time(), 0
solfound = False

"""
We pick two numbers a and b, so that 99 >= a >= b >= 2. We tell Mr. P. the product a x b and Mr. S. the sum a + b. Then Mr. S. and Mr. P. engage in the following dialog:

Mr. P.: I don't know the numbers.
Mr. S.: I knew you didn't know. I don't know either.
Mr. P.: Now I know the numbers.
Mr. S.: Now I know them too.

Find the numbers a and b.
"""
# limitations (a,b) in [2:100]
# P is the product a*b
# S is the sum a+b

# All possible solutions 
sols = []
for a in range(2,100):
	for b in range(a,100):
		sols.append([a,b, a*b, a+b, True])
		
print len(sols)

non_valid_p =[]
non_valid_s =[]

# after the first conversation since the Mr P didn't know the numbers so P cannot be a product of two unique numbers (primes)
for x in sols :
	if isPrime(x[0]) and isPrime(x[1]) :
		non_valid_p.append(x[0]*x[1])
		#print x[0], x[1], x[0]*x[1]
		x[4] = False

count = 0 
for x in sols :
	if x[4] :
		#print x
		count += 1
#print count

# when Mr S states that he knows that Mr P didn't know 
# it meant that all his options for the sum had more than one product solution		

# Checking invalid sums 
sum_sols = []

for x in range(4,199):
	for y in range(2,x/2+1) :
		if y > 99 : break
		if isPrime(y) and isPrime(x-y): 
			non_valid_s.append(x)
			break
			

for x in sols :
	if x[3] in non_valid_s : x[4] = False
		

count = 0		
for x in sols :
	if x[4] :
		#print x
		count += 1
print count

for x in sols : 
	#if x[4] and (x[0] == 4): print x
	if x[4] : print x

print '*'*65
print "**  Answer   :\t{0}\n**  Found in :\t{1} ".format(sol, time.time() - starttime)
print '*'*65


