import time
starttime,sol = time.time(), 0

nmax = 1000000
b = [True for i in range(nmax+1)]
h = range(nmax+1)
for i in range(2,nmax+1):
        if b[i]:
                h[i]=i-1
                for j in range(2*i,nmax+1,i):
                        b[j] = False
                        h[j] = h[j]*(i-1)//i
sol =  sum(h[2:])

print "*****************************************************************"	
print "**  Answer   :\t{0}\n**  Found in :\t{1} ".format(sol, time.time() - starttime)
print "*****************************************************************"	
# A 303963552391 T 58.5789999962