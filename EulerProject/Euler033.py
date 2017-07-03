import time
starttime,sol = time.time(), 0

def gcd(a, b):
    while b != 0:
        (a, b) = (b, a%b)
    return a

n = d = 1
for a in  range(1,10):
	for b in  range(1,10):
		for c in  range(1,10):
			x = a*10 + c
			y = c*10 + b
			if x >= y : continue		
			if not gcd(x,y) == 1:
				if x * b == y *a:
					n *= x
					d *= y

sol = d/gcd(n,d)

print "\n*****************************************************************"	
print "**  Answer   :\t{0}\n**  Found in :\t{1} ".format(sol, time.time() - starttime)
print "*****************************************************************"	
# CA 100 T 0.00300002098083
# CA 100 T 0.00200009346008




