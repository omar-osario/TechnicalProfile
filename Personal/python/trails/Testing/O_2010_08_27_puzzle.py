import time
from mth import *
from gen import *
from math import sqrt
starttime,sol = time.time(), 0
solfound = False

"""
In ancient China, two thousand years ago, a general wanted to count his troops. He first had them line up in ranks of eleven, and there were ten troops left over in the last rank. Then he had his troops line up in ranks of twelve, and there were four left over in the last rank. Finally he had them line up in ranks of thirteen, and there were twelve troops remaining in the last rank.

"""
for x in range(21,10000,11):
	if x % 12 == 4 :
		if x % 13 == 12 :
			print x
	
	
print '*'*65
print "**  Answer   :\t{0}\n**  Found in :\t{1} ".format(sol, time.time() - starttime)
print '*'*65


