import time
import sys
starttime,sol = time.time(), 0

# adding a base element to a list of elements and returning the new list
def addelemenetsstr(base,arr) :
    temp =[]
    for x in arr:
        temp.append(base+","+x)
    return temp
   
# removes all repetition in the string i.e 2,2 -> 4
def removerep(line) :
    elem = line.split(',')
    rep = True
    while ( rep ) :
        rep = False    
        for x in range(1,len(elem)) :
            # Checking for repetition
            if elem[x-1] == elem[x] :
                # replacing two
                #print (elem[x-1],elem[x],"-->",(2*int(elem[x-1])))
                elem[x-1:x+1] = [str(2*int(elem[x]))]
                rep = True    
                break
    return elem
   
# Calculate the average maximum number in the array
def calculateavg(lst) :
    res=0.0
    for line in lst :
        nonrep = (removerep(line))
        maxvalue = float(max(nonrep))
        weight = pow(.5, len(line.split(',')))
        res +=  maxvalue*weight
    return res    
     
elements = ['2','4']
resultlist = ['2','4']
desireddepth = 5
complete=False
start=0
while not complete :
    change = False
    for x in range(start,len(resultlist)) :
        temp = removerep(resultlist[x])
        #print (".", end=""),
        if  len(temp) < desireddepth :
            #print("BAD: ",resultlist[x])
            resultlist[x:x+1] = addelemenetsstr(resultlist[x],elements)
            change = True
            break
        start = x +1
        #print("GOOD: ",resultlist[x])
    # If no changes have been
    if  not change:
        complete = True
       
print ("*")
for x in resultlist :
    print( x)
sol = calculateavg( resultlist)
print
print ("*****************************************************************")
print ("**  Answer   :\t{0}\n**  Found in :\t{1} ".format(sol, time.time() - starttime))
print ("*****************************************************************")
