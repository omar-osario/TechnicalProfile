digit_precendence = dict()
 
for line in [line.strip() for line in open("./keylog.txt")]:
    for index, char in enumerate(line):
        digits = digit_precendence.setdefault(int(char), set())
        if index < len(line)-1:
            digits.add(int(line[index+1]))
 
print "digraph problem79 {"
for (digit, subsequent_digits) in digit_precendence.iteritems():
    for subsequent_digit in subsequent_digits:
        print "   %d -> %d;" % (digit, subsequent_digit)
print "}"