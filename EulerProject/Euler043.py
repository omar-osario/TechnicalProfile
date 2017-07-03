import time
from math import sqrt
import operator 
starttime,sol = time.time(), 0

def isPandigital(n, l):
	temp = str(n)
	for x in range(0,10):
		if not str(x) in temp: return False
	return True

def hasRepeatedDigit(n):
	temp = str(n)
	for x in temp:
		if temp.count(x) > 1 :return True 
	return False

	
def hasSpecialProperty(n):
	temp = str(n)
	if int(temp[3])%2 != 0 : return False
	if int(temp[2:5]) % 3 != 0 : return False
	if int(temp[5])%5 != 0 : return False
	if int(temp[4:7]) % 7 != 0 : return False
	if int(temp[5:8]) % 11 != 0 : return False
	if int(temp[6:9]) % 13 != 0 : return False
	if int(temp[7:]) % 17 != 0 : return False
	return True
	
temp = []
#for i in range(10000,99999):
for i in range(0,999999):
	if (i%1000) % 17 != 0 : continue
	if ((i%10000)/10) % 13 != 0 : continue
	if ((i%100000)/100) % 11 != 0 : continue
	if ((i%1000000)/1000) % 7 != 0 : continue
	if ((i%10000000)/10000) % 5 != 0 : continue
	if hasRepeatedDigit(i) : continue

	temp.append(i)

#for x in temp:
	#print x, hasRepeatedDigit(x)

for a in temp :
	for x in [1,3,4,6]:
		if str(x) in str(a) : continue
		for y in [0,1,3,4,6]:
			if str(y) in str(a) : continue
			if y == x :continue
			for z in [0,1,3,4,6]:
				if str(z) in str(a) : continue
				if z == x or z == y: continue 
				for q in [0, 2, 4, 6, 8]:
					if q == x or q == y or q ==z: continue 
					if str(q) in str(a) : continue
					
					dummy = x*(10**9) + y*(10**8) + z*(10**7) + q*(10**6) + a
					if hasSpecialProperty(dummy):
						if isPandigital(dummy,10):
						#	print x, y , z, dummy
							sol += dummy
			
	
print "\n*************************************************"	
print "**  Answer   :\t{:>25}      **".format(sol)
print "**  Found in :\t{:>25}      **".format(time.time() - starttime)
print "*************************************************"
# W 5512714578 T 1.63800001144
# A 16695334890 T 2.05900001526
# A 16695334890 T 1.85599994659
# A 16695334890 T 1.80900001526
# A 16695334890 T 0.233999967575
# A 16695334890 T 0.203000068665
# A 16695334890 T 0.201999902725
# A 16695334890 T 0.171999931335






