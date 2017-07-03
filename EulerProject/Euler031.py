"""
In England the currency is made up of pound, , and pence, p, and there are eight coins in general circulation:

1p, 2p, 5p, 10p, 20p, 50p, P1 (100p) and P2 (200p).
It is possible to make P2 in the following way:

1Px1 + 1x50p + 2x20p + 1x5p + 1x2p + 3x1p
How many different ways can P2 be made using any number of coins?
"""

from math import *
import time
starttime,sol = time.time(), 0
target = 200

for a in range(target, -1,-200):
	for b in range(a, -1,-100):
		for c in range(b, -1,-50):
			for d in range(c, -1,-20):
				for e in range(d, -1,-10):
					for f in range(e, -1,-5):
						for g in range(f, -1,-2):
								sol += 1
	
	


print "\n*****************************************************************"	
print "**  Answer   :\t{0}\n**  Found in :\t{1} ".format(sol, time.time() - starttime)
print "*****************************************************************"	
# CA 73682 T 0.0119998455048




