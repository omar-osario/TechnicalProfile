import time 
starttime = time.time()
solfound,sol = False, 0

def gcd(a,b):
	while b: a, b = b, a%b
	return a


e = [2]
for x in range(1,34) :
	e.append(1)
	e.append(2*x)
	e.append(1)
	
def contFracRationalApproxFore(n):
	if n < 1 : return [-1, -1] 
	if n == 1 : return [2, 1]
	num = 1
	den = e[n-1]
	for x in range(n-2,0,-1):	
		temp_d = den 
		den = e[x]*den + num 
		num = temp_d

	num = e[0]*den + num
	com = gcd(num, den)
	return [num/com, den/com]

for x in str(contFracRationalApproxFore(100)[0]):
	sol += int(x)

	

print "\n*************************************************"	
print "**  Answer   :\t{:>25}      **".format(sol)
print "**  Found in :\t{:>25}      **".format(time.time() - starttime)
print "*************************************************"
# A 272 T 0.0100002288818
# A 272 T 0.00399994850159