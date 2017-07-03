import time
from mth import *
from gen import *
from math import sqrt
starttime,sol = time.time(), 0
solfound = False

def politeness(n):

	politeness = 0
	# finding the limit on the tests 
	limit = n 
	while True :
		if isSquare(8*limit + 1) : 
			limit = (sqrt(1 + 8*limit) - 1.0)/2.0
			break
		limit += 1
	
	# Going through the test 
	for x in range ( 2, int(limit) + 1):	
		test = 0
		if x % 2 == 0 : test = x / 2	
		if n % x == test : 
			politeness += 1
		
	return politeness


		
for x in range(1,10101):
	#if isTriangularNumber(x) : print x, 
	#if x% 7 == 0 : print
	if politeness(x) > 20  : print x, politeness(x)
	
print
print '*'*65
print "**  Answer   :\t{0}\n**  Found in :\t{1} ".format(sol, time.time() - starttime)
print '*'*65


