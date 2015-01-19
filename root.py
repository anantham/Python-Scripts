# btw I KNOW that import math.sqrt() and sqrt(<number>) can do this :p
resp="n"
while(not(resp=="y" or resp=="Y")):
    print "Enter the number of which u want to find root (greater than 1)"
    userinput=raw_input()
    
    length=len(userinput)
    try:
        no=int(userinput)
    except ValueError:
        print "INVALID INPUT!!!! Exiting program"
        break
    if(no<1):
        print "Please enter number greater than 1"
        break
    
    print "Enter the no of decimals to which u want to find root, Maximum 11 digits"
    try:
        deci=int(raw_input())
    except ValueError:
        print "INVALID INPUT!!!! Exiting program"
        break
    
    if(deci>11):
        print "sorry This script cannot perform that function, sorry"
        # We can increase this using the decimal module.
        break
    
    #now we need to get the intial amount by which ans should be varied if no is a single
    #digit no then by .1 if its a n digit no then by 10 to the power n-1
    if length==1:
        multi=10**(-2)
    elif length>1:
        multi=10**(length-3)
    ans=no/2
    
    #to find root(no) to a high degree of precision
    while(not(len(str(ans))==deci+length+1)):
        #if the point at which if we add prec*opti we overshoot and if we subtract we undersell..
        #then we optimize the number that is added, ie make it smaller
        
        #basically better way to do this, use patterns
        if( ans**2<no and (ans+multi)**2>no):
            multi=multi/10
            print "optimizing search for root"
        #other wise continue to find the number at that decimal place
        if((ans*ans)>no):
           ans=ans-multi
           print "working...."
        elif((ans*ans)<no):
            ans=ans+multi
            print "working...."
        if((ans*ans)==no):
            break
        
        print "please wait....."
        

    #we have found the root within the precision defined
    print "The root of "+str(no)+" is "+str(ans)

    print "Do You want to exit the program??! y/n"
    resp=raw_input()

dummy = raw_input()

