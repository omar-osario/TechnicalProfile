"""
A permutation is an ordered arrangement of objects. For example, 3124 is one possible permutation of the digits 1, 2, 3 and 4. If all of the permutations are listed numerically or alphabetically, we call it lexicographic order. The lexicographic permutations of 0, 1 and 2 are:

012   021   102   120   201   210

What is the millionth lexicographic permutation of the digits 0, 1, 2, 3, 4, 5, 6, 7, 8 and 9?
"""

from math import *
import time
starttime,sol = time.time(), 0

elements = range(0,10)
facts = [factorial(i) for i in range(0,10)]
numofelements = len(elements)
rank = 1000000
testrank = 0 
finalnumber = ""

for i in range(numofelements-1,0,-1):	
	tempdigit = 0

	while (testrank + facts[i]) < rank :
		testrank += facts[i]
		tempdigit += 1
	
	finalnumber += str(elements[tempdigit])
	elements.remove(elements[tempdigit])
	
finalnumber += '0'		
sol = int(finalnumber)

	
print "\n*****************************************************************"	
print "**  Answer   :\t{0}\n**  Found in :\t{1} ".format(sol, time.time() - starttime)
print "*****************************************************************"	
# CA 2783915460 T 0.108999967575
# CA 2783915460 T 0.0149998664856
# CA 2783915460 T 0.0


