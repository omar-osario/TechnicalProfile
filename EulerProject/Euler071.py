import time
import sys
import string
from math import *
starttime,sol = time.time(), []


def gcd(a,b):
	while b: a, b = b, a%b
	return a

exact_num = 0.42857142857142855
pairs = [[0.42857142857142855,3,7]]

for x in range(990000,1000000):
	lower = int(float(x)*exact_num) - 1
	if gcd(lower,x) == 1: pairs.append([float(lower)/float(x), lower, x])			
pairs = sorted(pairs)

for x in range(len(pairs)-1, 0, -1) :
	if pairs[x][1] == 3 and  pairs[x][2] == 7:
		sol = pairs[x-1][1]
		break
		
print "*****************************************************************"	
print "**  Answer   :\t{0}\n**  Found in :\t{1} ".format(sol, time.time() - starttime)
print "*****************************************************************"	
#13.3489999771
#6.8639998436
#3.99399995804
#3.33800005913
#0.266000032425
#0.0160000324249


"""
for x in range(10,40000):
	digits = len(str(x))-1
	lower = int(lowerLimit(digits)*float(x))/(10**(digits-1))
	if lower == 0: continue
	upper = lower + 10**(digits)/2 
	#print lower, upper , x
	for y in range(lower,upper):
		if gcd(y,x) == 1: 
			temp = float(y)/float(x)
			pairs.append([temp, y, x])			
	#y = lower +1
	#if gcd(y,x) == 1: 
	#	temp = float(y)/float(x)
	#	pairs.append([temp, y, x])			
"""		

"""
upperlimit = 0.4285715
lowerlimit = 0.4285713
pairs =[0.42857142857142855, 3, 7]
	
for x in range(10,1000001,2):
	if x % 10000 == 0 : print ".",
	rangeupper = 4288*x/10000
	rangelower = 4286*x/10000
	for y in xrange(rangelower, rangeupper):
		temp = float(y)/float(x)
		if temp < lowerlimit or temp > upperlimit: continue
		if gcd(y,x) == 1: 
			pairs.append([temp, y,x,])
			print temp , y, x
		
pairs = sorted(pairs)
#for x in pairs :
#	print pairs
"""