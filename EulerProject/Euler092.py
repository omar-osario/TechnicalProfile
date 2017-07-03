import time
starttime,sol = time.time(), 0

values = [ 0, 1, 4, 9, 16, 25, 36, 49, 64, 81 ]
onedigitfactiorials = [ 1, 1, 2, 6, 24, 120, 720, 5040, 40320,362880, 3628800 ]

def calculatePermutation(n):
	count = [ 0, 0, 0, 0, 0, 0, 0, 0, 0, 0 ]
	dummy = 1
	for x in str(n):
		count[int(x)]+= 1
	
	for x in count:
		dummy *=onedigitfactiorials[x]
		
	return onedigitfactiorials[len(str(n))]/dummy 
	
def squareChain(n) :
	next = n 
	temp = 0 
	while next != 1 and next != 89 : 
		for x in str(next):
			temp += values[int(x)]
		next = temp
		temp = 0 
	return next

temp  = ""
for a in range(9,-1,-1) :
	for b in range(a,-1,-1) :
		for c in range(b,-1,-1) :
			for d in range(c,-1,-1) :
				for e in range(d,-1,-1) :
					for f in range(e,-1,-1) :
						for g in range(f,-1,-1) :
						#	print '.',
							temp = int(str(a)+str(b)+str(c)+str(d)+str(e)+str(f)+str(g))
							if temp == 0 : continue
							if squareChain(temp) == 89: 
						#		print '#',
								sol += calculatePermutation(temp)


print "\n*****************************************************************"	
print "**  Answer   :\t{0}\n**  Found in :\t{1} ".format(sol, time.time() - starttime)
print "*****************************************************************"	
# X 4280 T 0.16504506307 (Approx)
# X 9814 T 33.1949999332
# X 4622070 T 0.30999994278
# X 4622070 T 0.30999994278
# A 8581146 T 2.80100011826
# A 8581146 T 0.31900000572
# A 8581146 T 0.31299996376

