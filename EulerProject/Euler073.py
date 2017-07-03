import time
import sys
import string
from math import *
starttime,sol = time.time(), 0


def gcd(a,b):
	while b: a, b = b, a%b
	return a


	

lowerlimit = 0.333333333333333333
upperlimit  = 0.5

for x in range(5,12001):
	
	for y in range(int(float(x)*lowerlimit), int(float(x)*upperlimit)+1):
		if gcd(y,x) == 1: 
			temp = float(y)/float(x)
			if temp > lowerlimit and temp < upperlimit:
				sol += 1

		
print "*****************************************************************"	
print "**  Answer   :\t{0}\n**  Found in :\t{1} ".format(sol, time.time() - starttime)
print "*****************************************************************"	
# tried 7294838 in 46.503000021 -- wrong
# tried 7295372 in 19.364000082 -- right

