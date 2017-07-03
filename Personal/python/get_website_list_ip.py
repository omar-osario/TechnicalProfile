import net
from gen import *

websites = filetostrlist('C:/m_lib/net/website.list')
filename = str('[website_ips] ' + t(tf_filename) + '.txt')
file = open('C:/m_lib/info/' + filename, 'w')

for website in websites :
	print >> file, '='*(len(website) + 12)
	print >> file,str('----[ ' +  website + ' ]----')
	print >> file,'='*(len(website) + 12)
	
	for ip in sorted(net.getallipv4(website)) : 
		ll = 30 - len(ip[1]) 
		print >> file,str(ip[1] + ' '*ll + ip[0])
	
	print >> file,'-'*(len(website) + 12),'\n'