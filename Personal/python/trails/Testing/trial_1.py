import time
import sys
import string
starttime,sol = time.time(), 0
def letterToT9(n, res = ""):
	past = "-"
	for x in n:
		if past[-1] == T9[x][0]:
			res += " "
		res +=  T9[x]
		past = T9[x]
	return res

T9 = dict([['a', '2'], ['b', '22'], ['c', '222'], ['d', '3'], ['e', '33'], ['f', '333'], ['g', '4'], ['h', '44'], ['i', '444'], ['j', '5'], ['k', '55'], ['l', '555'], ['m', '6'], ['n', '66'], ['o', '666'], ['p', '7'], ['q', '77'], ['r', '777'], ['s', '7777'], ['t', '8'], ['u', '88'], ['v', '888'], ['w', '9'], ['x', '99'], ['y', '999'], ['z', '9999'], [' ','0']])

file_1 = open('trial_1_C-large-practice.in','r')
file_2 = open('trial_1_L_sol.txt', 'w')

numoflines = int(file_1.readline())	

for x in range(numoflines):
	print >> file_2,"Case #{0}: {1}".format(x+1, letterToT9(file_1.readline()[0:-1]).strip())



print "================================================================"	
print "Answer ", sol, "found in", time.time() - starttime
print "================================================================"	