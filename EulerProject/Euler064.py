import time 
from math import sqrt
starttime = time.time()
solfound,sol = False, 0
def calculateContFractionSqrt(n):
	
	i = 0 
	dummy = sqrt(n)
	if int(dummy) == dummy : return -1
	periodfound = False
	a_s = int(dummy)
	b_s = 1
	x_n = x_n_s = a_s
	x_d = x_d_s = n - x_n_s**2
	
	print str('sqrt(' + str(n) + ') = [(' + str(a_s) + ')' ),
	while not periodfound :
		a = int(sqrt(n) + x_n)/x_d
		x_n = (a*x_d - x_n)
		x_d = (n - x_n**2)/x_d 
		i += 1
		print str( ', ' + str(a)),
		if x_n == x_n_s and x_d == x_d_s :
			periodfound = True
	#		return i 
			print str(']')

def lenghtOfContFractionSqrt(n):
	
	i = 0 
	dummy = sqrt(n)
	if int(dummy) == dummy : return 0
	a_s = int(dummy)
	x_n = x_n_s = a_s
	x_d = x_d_s = n - x_n_s**2
	periodfound = False
	
	while not periodfound :
		a = int(sqrt(n) + x_n)/x_d
		x_n = (a*x_d - x_n)
		x_d = (n - x_n**2)/x_d 
		i += 1
		if x_n == x_n_s and x_d == x_d_s :
			return i 

for x in range (4, 10001 ,3):
	if lenghtOfContFractionSqrt(x)%2 == 1 : sol += 1
	if lenghtOfContFractionSqrt(x+1)%2 == 1 : sol += 1


print "\n*************************************************"	
print "**  Answer   :\t{:>25}      **".format(sol)
print "**  Found in :\t{:>25}      **".format(time.time() - starttime)
print "*************************************************"
# A 1322 T 0.194999933243
# A 1322 T 0.146999835968
