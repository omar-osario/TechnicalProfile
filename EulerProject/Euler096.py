import time 
starttime = time.time()
solfound,sol = False, 0
SIZE = 9

def sodukoBasicTest(element):
	for e in element :
		if e[0] == 0 : continue
		else :
			for x in range(SIZE):
				if x == e[0]-1 : continue
				e[1][x] = 0
	return
	
def sodukoNineTest(element):
	for e in element :
		base = e[0]
		if base == 0 : continue
		else :
			for a in element:
				if sum(a[1]) == 1 : continue
				a[1][base-1] = 0
	return

test = [ 	'003020600',
			'900305001',
			'001806400',
			'008102900',
			'700000008',
			'006708200',
			'002609500',
			'800203009',
			'005010300']

temp = []

for a in test :
	dummy = []
	for b in a.strip() :
		dummy.append([int(b)])
	temp.append(dummy)
	
#rowTest(temp[0])
for a in temp:
	for b in a :
		b.append([1 for i in range(SIZE)])


print '*'*8
for x in temp :
	sodukoBasicTest(x)
	sodukoNineTest(x)
print '*'*8

temprow = []

for a in range(SIZE):
	for b in range(SIZE):
		temprow.append(temp[b][a])
	print '*'*8
	
for a in temprow :
	for b in a : print b
	print '*'*8

"\n*************************************************"	
print "**  Answer   :\t{:>25}      **".format(sol)
print "**  Found in :\t{:>25}      **".format(time.time() - starttime)
print "*************************************************"
# A