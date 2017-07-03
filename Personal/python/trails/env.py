import os
import stat
from time import *
from gen import *
import net


line = 100 
current_path = 'C:/Users/IBM_ADMIN/Documents/Scripting/Python/'
test_path ='C:/Users/IBM_ADMIN/Documents/Scripting/Python/'

# Environment variables
for x in os.environ:
	print '=====[', x , ']====='
	for y in os.environ[x].split(';'): print y
	
print '='*line
print '='*line


