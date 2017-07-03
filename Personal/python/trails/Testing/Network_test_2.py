import time
import sys
import string
import socket

starttime,sol = time.time(), 0



oct_1 = '136'
oct_2 = '186'
oct_3 = '1'
base = '.'.join((oct_1, oct_2, oct_3))
valid_IPs = []
file = open('net_res.txt','w')
for oct_x in range(1,254):
	temp = '.'.join((base, str(oct_x)))
	print 'validating with', temp, " ... ",
	try :
		info = socket.gethostbyaddr(temp)
	except socket.herror , msg:
		print 'BAD'
		continue
	print 'GOOD'
	valid_IPs.append([info[2], info[0]])

for x in valid_IPs :
	print >> file, x[0], '\t', x[1]
	print x[0], '\t', x[1]
print "================================================================"	
print "Answer ", sol, "found in", time.time() - starttime
print "================================================================"	