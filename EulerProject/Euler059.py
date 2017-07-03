import time 
from operator import xor
from collections import Counter
starttime = time.time()
solfound,sol = False, 0

lengthofpass = 3
# no symbols in the report
llimit = ord(' ')
ulimit = ord('z')
f = open('cipher1.txt','r')
temp = f.read()

lettercounter = Counter()
encrypted = temp.split(',')
code = [[] for i in range(lengthofpass)]
message = ''
for i in range(lengthofpass):
	for a in range(llimit, ulimit+1):
		for l in range(i,len(encrypted),lengthofpass):
			temp = xor(int(encrypted[l]),a)
			if temp < llimit or temp > ulimit :	break
			if l > len(encrypted) - ( lengthofpass + 1):
				print l, a , chr(a), temp, chr(temp) , len(encrypted)
				code[i].append(chr(a))
print code

for x in code[0]:
	for y in code[1]:
		for z in code[2]:
			message = ''
			for a in range(len(encrypted)):
				if a % 3 == 0 :	decrypt = x
				if a % 3 == 1 :	decrypt = y
				if a % 3 == 2 :	decrypt = z
				message += chr(xor(int(encrypted[a]),ord(decrypt)))
			print message
			print
	
for x in message :
	sol += ord(x)
print "\n*************************************************"	
print "**  Answer   :\t{:>25}      **".format(sol)
print "**  Found in :\t{:>25}      **".format(time.time() - starttime)
print "*************************************************"
# A 107359 T 0.158999919891
# A 107359 T 0.0520000457764





