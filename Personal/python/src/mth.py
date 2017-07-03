from math import sqrt
SUITPRIMES = [2,3,5,7]

__all__ = ["e_1000", "p_1000", "triangular", "square", "pentagonal", "hexagonal", "octagonal", "isPrime", "isSquare", "gcd", "isPandigital", "hasRepeatedDigit", "isTriangularNumber", "isSquareNumber", "isPentagonalNumber", "isHexagonalNumber", "isHeptagonalNumber", "isOctagonalNumber", "relativePrimes", "isPermutation", "numberOfRelativePrimes", "contFracRationalApproxFore", "sumOfDigits", "ContFractionSqrt", "isHappyNumber", "politeness"]

e_1000 = '27182818284590452353602874713526624977572470936999595749669676277240766303535475945713821785251664274274663919320030599218174135966290435729003342952605956307381323286279434907632338298807531952510190115738341879307021540891499348841675092447614606680822648001684774118537423454424371075390777449920695517027618386062613313845830007520449338265602976067371132007093287091274437470472306969772093101416928368190255151086574637721112523897844250569536967707854499699679468644549059879316368892300987931277361782154249992295763514822082698951936680331825288693984964651058209392398294887933203625094431173012381970684161403970198376793206832823764648042953118023287825098194558153017567173613320698112509961818815930416903515988885193458072738667385894228792284998920868058257492796104841984443634632449684875602336248270419786232090021609902353043699418491463140934317381436405462531520961836908887070167683964243781405927145635490613031072085103837505101157477041718986106873969655212671546889570350354'

p_1000 = '31415926535897932384626433832795028841971693993751058209749445923078164062862089986280348253421170679821480865132823066470938446095505822317253594081284811174502841027019385211055596446229489549303819644288109756659334461284756482337867831652712019091456485669234603486104543266482133936072602491412737245870066063155881748815209209628292540917153643678925903600113305305488204665213841469519415116094330572703657595919530921861173819326117931051185480744623799627495673518857527248912279381830119491298336733624406566430860213949463952247371907021798609437027705392171762931767523846748184676694051320005681271452635608277857713427577896091736371787214684409012249534301465495853710507922796892589235420199561121290219608640344181598136297747713099605187072113499999983729780499510597317328160963185950244594553469083026425223082533446850352619311881710100031378387528865875332083814206171776691473035982534904287554687311595628638823537875937519577818577805321712268066130019278766111959092164201989'

triangular = lambda n : n*(n+1)/2
square = lambda n : n**2
pentagonal = lambda n : n*(3*n-1)/2
hexagonal  = lambda n : n*(2*n-1)
heptagonal  = lambda n : n*(5*n-3)/2
octagonal  = lambda n : n*(3*n-2)

def isPrime(n):
	if n == 1 : return False
	if n in SUITPRIMES : return True

	for x in SUITPRIMES :
		if n%x == 0 :
			return False
	
	upperlimit = int(sqrt(n))	
	
	for x in xrange(9,upperlimit +1,2) :
		if n%x == 0:
			return False 

	if n == 1 : return False
	return True

def isSquare(n):
	temp = sqrt(n)
	return temp == int(temp)		
	
def gcd(a,b):
	while b: a, b = b, a%b
	return a

def isPandigital(n, l = 9):
	temp = str(n)
	for x in range(0,l + 1):
		if not str(x) in temp: return False
	return True

def hasRepeatedDigit(n):
	temp = str(n)
	for x in temp:
		if temp.count(x) > 1 :return True 
	return False

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
		
def relativePrimes(n):

	dummy = 0 
	if isPrime(n) : return []
	
	upperlimit = sqrt(n)
	if upperlimit == int(upperlimit) : dummy = 1
	
	res = n
	f=[]
	for x in range(2, int(upperlimit) + 1) :
		if n%x == 0 : f.append(x)

	for x in f[:dummy:-1] : f.append(n/x) 
	p = [i for i in f if isPrime(i)]
	
	return p 
	
def isPermutation(n,m):
	tempa, tempb = str(n), str(m)
	if len(tempa) != len(tempb) : return False
	a, b = Counter(), Counter()
	for x in range(len(tempa)):
		a[tempa[x]] += 1
		b[tempb[x]] += 1
	if a == b : return True
	return False

def numberOfRelativePrimes(n):
	
	f = []
	if isPrime(n) : return float(n-1)
	upperlimit = sqrt(n)
	if upperlimit == int(upperlimit) : 
		return float((n*numberOfRelativePrimes(upperlimit))/upperlimit)
	
	res = n
	for x in range(2, int(upperlimit) + 1) :
		if n%x == 0 : f.append(x)

	for x in f[::-1] : f.append(n/x) 
	p = [i for i in f if isPrime(i)]
	
	for x in p :
		res *= x-1
		res /= x
	return float(res)

def contFracRationalApproxFore(n):

	e = [2]
	for x in range(1,n/3+2) :
		e.append(1)
		e.append(2*x)
		e.append(1)
		
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

def sumOfDigits(n):
	temp = str(n)
	sum = 0 
	for x in temp: sum += int(x)
	return sum
	
def ContFractionSqrt(n):
	
	dummy = sqrt(n)
	if int(dummy) == dummy : return [int(dummy)]
	periodfound = False
	a_s = int(dummy)
	b_s = 1
	x_n = x_n_s = a_s
	x_d = x_d_s = n - x_n_s**2
	temp_sol = [a_s , []]

	while not periodfound :
		a = int(sqrt(n) + x_n)/x_d
		x_n = (a*x_d - x_n)
		x_d = (n - x_n**2)/x_d 
		temp_sol[1].append(a)
		
		if x_n == x_n_s and x_d == x_d_s :
			periodfound = True
			return temp_sol
			
def isHappyNumber(n):

	temp_sum = []
	temp_str= str(n)
	while True:
		temp = 0
		for i in temp_str :
			temp += int(i)**2
		
		# Happy Number 
		if temp == 1 : 	return True
		
		# Sad Number 
		if temp in temp_sum : return False

		#Add the number to the Chain
		temp_sum.append(temp)
		
		temp_str = str(temp)		

def politeness(n):

	politeness = 0
	# finding the limit on the tests 
	limit = n 
	while True :
		if isSquare(8*limit + 1) : 
			limit = (sqrt(1 + 8*limit) - 1.0)/2.0
			break
		limit += 1
	
	# Going through the test 
	for x in range ( 2, int(limit) + 1):	
		test = 0
		if x % 2 == 0 : test = x / 2	
		if n % x == test : 
			politeness += 1
		
	return politeness		