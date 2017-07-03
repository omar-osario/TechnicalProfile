import time
import sys
import string
import os 
from decimal import *
from math import sqrt
import zlib
starttime,sol = time.time(), 0


s_1 = 'witch which has which witches wrist watch'
t_1 = zlib.compress(s_1)
print len(s_1)
print len(t_1)
s_2 = zlib.decompress(t_1)
print s_2

sol = 112233445566778899

print
print "*****************************************************************"	
print "**  Answer   :\t{0}\n**  Found in :\t{1} ".format(sol, time.time() - starttime)
print "*****************************************************************"	