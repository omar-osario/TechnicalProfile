import time
import sys
import string
from math import *
starttime,sol = time.time(), 0
solfound = False
data_o = []
data = [319, 680, 180, 690, 129, 620, 762, 689, 762, 318, 368, 710, 720, 710, 629, 168, 160, 689, 716, 731, 736, 729, 316, 729, 729, 710, 769, 290, 719, 680, 318, 389, 162, 289, 162, 718, 729, 319, 790, 680, 890, 362, 319, 760, 316, 729, 380, 319, 728, 716 ]

#remove duplicates
for x in sorted(list(set(data))):
	data_o.append(str(x))

for a in data_o :
	passcode = a
	data_u = data_o
	print str('trying with ' + a)
	solfound = False
	trailtime = time.time()
	while not solfound :
		for x in data_u :
			if x in passcode :
				print str(x + ' removed')
				data_u.remove(x)
				break 
			if x[1:] == passcode[:2] : 
				passcode = x[0] + passcode
				data_u.remove(x)
				print str(x + 'removed')
				print str('password is now ' + passcode)

				break
			if x[:2] == passcode[-2:] : 
				passcode = passcode + x[2]
				data_u.remove(x)
				print str(x + ' removed')
				print str('password is now ' + passcode)

				break
			if x[-1] == passcode[0] : 
				passcode = x[:2] + passcode
				data_u.remove(x)
				print str(x + ' removed')
				print str('password is now ' + passcode)
				break
			if x[0] == passcode[-1] : 
				passcode = passcode + x[1:]
				data_u.remove(x)
				print str(x + ' removed')
				print str('password is now ' + passcode)
				break
		if time.time() - trailtime > 5: solfound = True
	print str('done with ' + a)
	print str('password was :' + passcode)
	print '======================================================='

print passcode
for x in data_u : print x
	
print "*****************************************************************"	
print "**  Answer   :\t{0}\n**  Found in :\t{1} ".format(sol, time.time() - starttime)
print "*****************************************************************"	
# questioon was misunderstood 

