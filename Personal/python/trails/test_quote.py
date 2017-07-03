# this prints outs random quote


import sys
from net import *
from gen import *

phrases = filetostrlist('C:/m_lib/gen/phrases.txt')

for x in phrases:
	print formatPhrase_1(x)
