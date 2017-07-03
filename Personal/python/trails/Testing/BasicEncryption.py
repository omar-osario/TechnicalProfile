from net import * 


offset = 13 

testscript = "abcdefghijklmnopqrstuvwxyz-ABCDEFGHIJKLMNOPQRSTUVWXYZ-0123456789-!\"#$%&'()*+,-./:;<=>?@[\\]^_`{|}~"
clear = testscript


"""		
	if x in string.digits : dcount += 1
	if x in specialchar : scount += 1
	initialindex = find(BASE,x)
	encoded += BASE[(initialindex + OFFSET)%len(BASE)] 
"""

#print net
print clear
encode = ceaserEncode(clear, offset)
print encode
decode = ceaserDecode(encode, offset)
print decode

"""
for x in encoded :
	if x == ' ' : 
		clear += ' '
		continue
	encodedindex = find(BASE,x)
	clear += BASE[(encodedindex - OFFSET)%len(BASE)] 

print "\n This is the original message \n", clear
"""