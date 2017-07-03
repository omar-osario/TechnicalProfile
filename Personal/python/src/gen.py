import sys
import os
import stat
from time import strftime 
from time import gmtime as gm 
from random import randint


tf = "%Y\\%m\\%d-%H:%M:%S"
tf_num = "%Y%m%d%H%M%S"
tf_file="%Y-%m-%d %H:%M:%S"
tf_filename="%Y%m%d_%H%M"

__all__ = ["filetostrlist", "filetointlist", "formatPhrase_1", "generatetxtfile_1", "getrandomfilename_1", "t", "basedir", "infodir","tf", "tf_num", "tf_file", "tf_filename","filesummary", "csfiletostrlist"]
		  
basedir = "C:/m_lib/"
infodir = "C:/m_lib/info"


def filesummary(file):
	temp = os.stat(file)
	det = [[file]]
	det.append(['C ' + t(tf_file,gm(temp.st_ctime))])
	det.append(['M ' + t(tf_file,gm(temp.st_mtime))])
	det.append(['S ' + str(temp.st_size/1024+1) + ' KB'])
	return det

def filetostrlist(file):
	temp = open(file,'r')
	lst = temp.read().split('\n')
	temp.close()
	return lst
	
def csfiletostrlist(file):
	temp = open(file,'r')
	lst = temp.read().split(',')
	temp.close()
	return lst

def filetointlist(file):
	temp = open(file,'r')
	lst = []
	for ins in temp.readlines() :
		lst.append(int(ins[:-1])) 
	temp.close()
	return lst

def formatPhrase_1(phrase):
	start, sen = phrase.split('_')
	l = start[0]
	ph = l.upper() + ' for ' + l.upper() + start[1:].lower() + ': ' + sen
	ph = ph.replace( l.upper(), '[' + l.upper() + ']').replace( l.lower(), '[' + l.lower() + ']')
	ph = ph.replace( '][' , '')
	return ph

def generatetxtfile_1(file,phraselist):
	tempfile = open(file + '.txt','w')
	for x in range(randint(3,20)):
		tempfile.write(formatPhrase_1(phraselist[x%len(phraselist)]) + '\n')
	tempfile.close()

def getrandomfilename_1(wordlist):
	tempname = 'RANDOMGENERATED_'
	tempname += str(randint(1000,9999)) + '_'
	tempname += wordlist[randint(0,len(wordlist)-1)].upper()
	return tempname
	
def t(format): 
	return strftime(format)