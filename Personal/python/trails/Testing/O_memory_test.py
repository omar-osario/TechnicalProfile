import os
import stat
import sys
from time import strftime
from time import ctime
timeformat = "%Y/%m/%d-%H:%M:%S"

numofstars = 100 
current_path = 'C:/Users/IBM_ADMIN/Documents/Scripting/Python/'
test_path ='C:/Users/IBM_ADMIN/Documents/Scripting/Python/Testing/'
f_1 = open('Helloworld.py','r')
f_2 = open('Stars.txt', 'r')

print '*'*numofstars
print f_1 
print f_2 
print '*'*numofstars

f1_stats = os.stat('Helloworld.py')
f2_stats = os.stat('Stars.txt')

print '*'*numofstars
print f1_stats
print '*'*numofstars
print f2_stats
print '*'*numofstars

print id(f_1) , sys.getsizeof(f_1)
print id(f_2) , sys.getsizeof(f_2)

"""
from ctypes import string_at
from sys import getsizeof
from binascii import hexlify
a = 0x7fff 
print(hexlify(string_at(id(a), getsizeof(a))))
"""



"""
print '*'*numofstars
for x in os.environ:
	print x, os.environ[x] , len(os.environ[x]) 

namesoffiles =[]	
print '*'*numofstars


for x in sorted(os.listdir(test_path)):
	if x[:2] == 'O_' : continue
	os.rename(test_path +  x, test_path + 'O_' + x)
for x in os.listdir(test_path):
	temp = os.stat(test_path + x)
	print x, 
	print '\tCreated on :',ctime(temp.st_ctime),
	print '\tModified on :', ctime(temp.st_mtime) , 
	print '\tSize : {:5} KB'.format(temp.st_size/1024+1)
temp_a = os.urandom(numofstars)
temp_b = os.urandom(numofstars)
temp_c = os.urandom(numofstars)
temp_d = os.urandom(numofstars)
temp_e = os.urandom(numofstars)
	
print '*'*numofstars
for x in range(numofstars):
	print "{:3}\t{:3}\t{:3}\t{:3}\t{:3}\t{:3}\t{:3}\t{:3}\t{:3}\t{:3}".format(ord(temp_a[x]), temp_a[x], ord(temp_b[x]), temp_b[x], ord(temp_c[x]), temp_c[x], ord(temp_d[x]), temp_d[x], ord(temp_e[x]), temp_e[x]),
	print
print
print '*'*numofstars
for x in os.urandom(numofstars):
	print ord(x),
print
print '*'*numofstars
for x in range(1,16):
	print x*x, chr(x*x)
print os.environ['USERNAME']
f_1.close()
f_2.close()
"""