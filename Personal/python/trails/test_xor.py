import time 
from operator import xor
from collections import Counter
starttime = time.time()
solfound,sol = False, 0

"""
def XorDecode(encrypted, key):
	elen = len(encrypted)
	klen =  len(key)
	secret = key
	clear = ""
	if klen < elen :
		secret *= ((elen/klen) + 1) 

	for a in range(elen):
		clear += chr(xor(int(ord(encrypted[a])),ord(secret[a])))
	return clear
"""
def XorEncode(msg, key):
	mlen = len(msg)
	klen =  len(key)
	secret = key
	encrypted = ""
	if klen < mlen :
		secret *= ((mlen/klen) + 1) 

	for a in range(mlen):
		encrypted += chr(xor(ord(msg[a]),ord(secret[a])))
	return encrypted		
	
	
clear ="Do you like Riddles my Lord ? Power resides where men believe it resides"
encoded = XorEncode(clear,"MMsmS")
clear_2 = XorEncode(encoded,"MMSmS ms")
clear_3 = XorEncode(encoded,"MMsmS")

print clear
print encoded
print clear_2
print clear_3


print "\n*************************************************"	
print "**  Answer   :\t{:>25}      **".format(sol)
print "**  Found in :\t{:>25}      **".format(time.time() - starttime)
print "*************************************************"
# A 107359 T 0.158999919891
# A 107359 T 0.0520000457764





