import time
starttime,sol = time.time(), 0
from math import sqrt
from mth import *

for i in xrange(160000,5000000,2):

	count = 0 
	if i % 10000 == 0 : print i 
	#print '='*20, i , '='*20
	#print str('[' + str(i+1) + ',' + str(i*(i+1)) +']')
	for j in range(i+2, 2*i):
		#if i % 2 == 1: break 
		if (i*j)%(j-i)	== 0 : 
			count += 1
	#		print str('[' + str(j) + ',' + str((i*j)/(j-i)) +']')
	#print str('[' + str(2*i) + ',' + str(2*i) +']')
	
	if count > 700 : print i, count, 
	elif count > 400 : print '#', 
	elif count > 200 : print '*',
	elif count > 100 : print '.',
	
	if count > 998 : 
		sol = i
		break

print "\n*****************************************************************"	
print "**  Answer   :\t{0}\n**  Found in :\t{1} ".format(sol, time.time() - starttime)
print "*****************************************************************"	
# A 180180 T 845.151000023


