import time
import sys
import string
from math import sqrt
starttime,sol = time.time(), 0

'5.2360679774997896964091736687313'
def firstThree(n):
	if n == 2:
		return '027'
	return str(int(float('5.2360679774997896964091736687313')**n))[-3::]
	
	
file_1 = open('trial_2_C-small-practice.in','r')
#file_2 = open('trial_2_sol.txt', 'w')
numoflines = int(file_1.readline())	
for x in range(numoflines):
	print "Case #{0}: {1}".format(x+1, firstThree(int(file_1.readline())))
	#print >> file_2,"Case #{0}: {1}".format(x+1, firstThree(int(file_1.readline())))


print 3.0 + sqrt(5.0)

print "================================================================"	
print "Answer ", sol, "found in", time.time() - starttime
print "================================================================"	