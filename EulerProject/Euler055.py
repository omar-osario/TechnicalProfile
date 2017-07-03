import time
import sys
import string
starttime,sol = time.time(), 0

def isLychrel(n):
	res = n + int(str(n)[::-1])
	for x in range(49):
		if str(res) == str(res)[::-1]: return 0
		res = res + int(str(res)[::-1])
	return 1

sol = sum(isLychrel(x) for x in range(10,10000))

print
print "*****************************************************************"	
print "**  Answer   :\t{0}\n**  Found in :\t{1} ".format(sol, time.time() - starttime)
print "*****************************************************************"	
#0.184000015259
#0.141999959946
#0.101999998093
#0.0980000495911
#0.0969998836517
#0.095999956131