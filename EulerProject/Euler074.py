import time
import sys
import string
from math import factorial

starttime,sol = time.time(), 0

def factorialChainLen(n) :
	f = []
	next = n 
	chain =  0
	temp = 0 
	while not next in f: 
		for x in str(next):
			temp += values[int(x)]
		f.append(next)
		chain += 1
		next = temp
		temp = 0 
	return chain

def factorialChain(n) :
	f = []
	next = n 
	chain =  0
	temp = 0 
	while not next in f: 
		for x in str(next):
			temp += values[int(x)]

		f.append(next)
		chain += 1
		next = temp
		temp = 0 
	return [f,chain]


values = [ 1, 1, 2, 6, 24, 120, 720, 5040, 40320,362880, 3628800 ]


"""
# slow method
ulimit = 1000000
for x in range(3,ulimit) :
	if x % 10000 == 0 : print '.',
	if factorialChainLen(x) == 60 :
		print x,
		sol += 1
"""
temp  = ""
for a in range(0,10) :
	for b in range(a,10) :
		for c in range(b,10) :
			for d in range(c,10) :
				for e in range(d,10) :
					for f in range(e,10) :
						temp = int(str(a)+str(b)+str(c)+str(d)+str(e)+str(f))
						if factorialChainLen(temp) == 60: print temp
					
print	
"*****************************************************************"	
print "**  Answer   :\t{0}\n**  Found in :\t{1} ".format(sol, time.time() - starttime)
print "*****************************************************************"	
# A 402 T 128.141000032
# A 402 T 119.387000084
# A 402 T 0.625999927521
#after the two results calcuate permutations and BAM the dirt is gone 


#						for g in range(f,10) :
#							for h in range(g,10) :
#								for i in range(h,10) :
#									for j in range(k,10) :
