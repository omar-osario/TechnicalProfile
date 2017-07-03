import time 
from math import sqrt
starttime = time.time()
solfound,sol = False, 0
#
# limits 4 digits so 
# tri = [45,140] 
# squ = [32,99] 
# pent = [26,81] 
# hex = [23,70] 
# hept = [21,63] 
# oct = [19,58] 
#
triangular = lambda n : n*(n+1)/2
square = lambda n : n**2
pentagonal = lambda n : n*(3*n-1)/2
hexagonal  = lambda n : n*(2*n-1)
heptagonal  = lambda n : n*(5*n-3)/2
octagonal  = lambda n : n*(3*n-2)

#triangulars = [triangular(i) for i in range(45,140)]
#squares = [square(i) for i in range(32,99)]
#pentagonals = [pentagonal(i) for i in range(26,81)]
#hexagonals = [hexagonal(i) for i in range(23,70)]
#heptagonals = [heptagonal(i) for i in range(21,63)]
octagons = [octagonal(i) for i in range(19,59)]



def isTriangularNumber(n):
	temp = (sqrt(1 + 8*n) - 1.0)/2.0
	return temp == int(temp)

def isSquareNumber(n):
	temp = sqrt(n)
	return temp == int(temp)	
	
def isPentagonalNumber(n):
	temp = (sqrt(1 + 24*n) + 1.0)/6.0
	return temp == int(temp)

def isHexagonalNumber(n):
	temp = (sqrt(1 + 8*n) + 1.0)/4.0
	return temp == int(temp)

def isHeptagonalNumber(n):
	temp = (sqrt(9 + 40*n) + 3.0)/10.0
	return temp == int(temp)

def isOctagonalNumber(n):
	temp = (sqrt(4 + 12*n) + 2.0)/6.0
	return temp == int(temp)
	

def testNumber(n, t):
	
	temp = []
	if t[0]: 
		if isTriangularNumber(n) : temp.append(0) 
	if t[1]: 
		if isSquareNumber(n) : temp.append(1)
	if t[2]: 
		if isPentagonalNumber(n): temp.append(2)
	if t[3]: 
		if isHexagonalNumber(n) : temp.append(3)
	if t[4]: 
		if isHeptagonalNumber(n) : temp.append(4)
	if t[5]: 
		if isOctagonalNumber(n) : temp.append(5)
	return temp
	
	
tests = [ True, True, True, True, True , True]
  
for a in range(19,59):
	if solfound : break
	tests[5] = False
	temp_a = octagonal(a)
	for b in range(10,100):
		temp_b = str(b)+str(temp_a)[:2]
		dummy_b = testNumber(int(temp_b),tests)
		if len(dummy_b) == 0 : continue 
		for x1 in dummy_b:
			tests[x1] = False
			for c in range(10,100):
				temp_c = str(c)+str(temp_b)[:2]
				dummy_c = testNumber(int(temp_c),tests)
				if len(dummy_c) == 0 : continue 
				for x2 in dummy_c:
					tests[x2] = False
					for d in range(10,100):
						temp_d = str(d)+str(temp_c)[:2]
						dummy_d = testNumber(int(temp_d),tests)
						if len(dummy_d) == 0 : continue 
						for x3 in dummy_d:
							tests[x3] = False
							for e in range(10,100):
								temp_e = str(e)+str(temp_d)[:2]
								dummy_e = testNumber(int(temp_e),tests)
								if len(dummy_e) == 0 : continue 
								for x4 in dummy_e:
									tests[x4] = False
									for f in range(10,100):
										temp_f = str(f)+str(temp_e)[:2]
										dummy_f = testNumber(int(temp_f),tests)
										if len(dummy_f) == 0 : continue 
										if temp_f[:2] == str(temp_a)[2:] :
											sol += int(temp_a) +int(temp_b) +int(temp_c) +int(temp_d) +int(temp_e) +int(temp_f)
											solfound = True
		
									tests[x4] = True
							tests[x3] = True
					tests[x2] = True
			tests[x1] = True
		

print "\n*************************************************"	
print "**  Answer   :\t{:>25}      **".format(sol)
print "**  Found in :\t{:>25}      **".format(time.time() - starttime)
print "*************************************************"
# A 28684 T  0.43799996376
# A 28684 T  0.0599999427795
# A 28684 T  0.0529999732971
