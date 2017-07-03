import time
import sys
import string
from math import sqrt as sqrt
from mth import *
starttime,sol = time.time(), 0
solfound = False

"""
print isPrime(61)
x = 2.15
d1 =  sqrt ( x*x + 61 - 12*x)
d2 =  sqrt ( x*x + 9)
print d1, d2 , d1 + d2
"""
a = 6
b = 5
c = 3



i = c**2
j = b**2*(2*a -1)
k = (a**2)*(b**2)*(-1)

print j**2 -4*i*k , isSquare(j**2 -4*i*k )

x = ((-1)*j + sqrt(j**2 - 4*i*k))/(2*i)
y = ((-1)*j - sqrt(j**2 - 4*i*k))/(2*i)
print x , y

path1 = sqrt(b**2 + x**2)
path2 = sqrt((a-x)**2 + c**2)

print path1, path2, path1 + path2

print "*****************************************************************"	
print "**  Answer   :\t{0}\n**  Found in :\t{1} ".format(sol, time.time() - starttime)
print "*****************************************************************"	
