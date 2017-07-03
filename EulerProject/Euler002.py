
from os import *
from shutil import *
from string import *

fib_a = 0 
fib_b = 1
fib_c = 1 
sum = 0
 
while fib_c < 4000000 :
	fib_a = fib_b
	fib_b = fib_c
	fib_c = fib_a + fib_b
	if fib_c > 4000000 :
		break
	if fib_c % 2 == 0  :
		sum += fib_c
print sum