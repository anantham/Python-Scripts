# This program is to implement the various methods taught in MA202 by Dr T.N.Janakiraman


# DEFINE FUNCTION IN THE CODE for now
# the polynomial is defined here
def poly(x):
    #return (x*x+x-pi*pi-pi)

    #from math import exp
    #return (exp(x)+x)

    return (x+5)*(x*x-5)

found = stop = False
digits = 4
pi = 3.1415926535897932384

# this function will give the x axis'x value at the point in the real line where the chord connecting the points  (a,poly(a)) and (b,poly(b)) cross the xaxis
def chord_xintercept(a,b):
    slope = (poly(b)-poly(a))/(b-a)
    
    x_a = a +  (-1*poly(a))/slope
    x_b = b - poly(b)/slope
    if(x_a == x_b):
        return x_a
    else:
        # debugging
        print "\nx_a = "+str(x_a)+" "+str(x_a==x_b)
        print "x_b = "+str(x_b)+"\n"
        return "done"
    
def regulafalsi(start,end):
    while(True):
        # the coreof this function, 
        var = chord_xintercept(start,end)
        
        # if we are lucky enough to be looking for a root
        # that can be described using a finte number of digits, and find it
        if(poly(start) == 0):
            return start
        if(poly(end) == 0):
            return end
        # if we have reached the last level of precision possible
        if(var == "done"):
            if(abs(poly(start))<abs(poly(end))):
                return start
            else:
                return end
   
        # Let us establish an alternate base condition, if the required level of precision has been reached,
        #if(poly(var) <= 10**(-1*digits) and poly(var) >= (-1*(10**(-1*digits)))):
            #return var

        # The root lies in between start and end, never play outside the boundaries :p 
        assert (poly(start)*poly(end) <= 0)
    
        # check on which side our var is on towards start or end?
        if( (poly(var)<0 and poly(start)<0) or (poly(var)>0 and poly(start)>0) ):
            # its on start's side, doesnt matter wheather thats positive or negative
            # we know that the root is between var and end, the new start is
            start = var
        else:
            # then var has to lie on the other side 
            end = var
        # for debuggind and letting the user know whats happening
        #print "\nThe start,end,var is "+str(start)+" "+str(end)+" "+str(var)
        #print "The start,end,var is "+str(poly(start))+" "+str(poly(end))+" "+str(poly(var))
        print "\nThe root lies between  "+str(start)+" AND "+str(end)+" \n working... shortening the range"

# the recursive function to find the root using Bisection Method-
# what we do is using the range the user helped us find, we start by
# finding the mid of that range and then check where this mid lies, wrt the root
# using this info we shorten the range by removing the redundant side of the range.
# we continue doing this by now finding the mid of the newly formed range.
def bisection(start,end):
    # recursion is not as fast I think. It will surely take more space as we go deeper,
    # I experienced "RuntimeError: maximum recursion depth exceeded while calling a Python object" thus i am now using a loop
    while(True):
        # the coreof this function, we use 2.0 to get var as a float
        var = (start+end)/2.0
    
        # if we are lucky enough to be looking for a root
        # that can be described using a finte number of digits, and find it
        if(poly(start) == 0):
            return start
        if(poly(end) == 0):
            return end
        # if we have reached the last level of precision possible
        if(start == end):
            return start
   
        # Let us establish an alternate base condition, if the required level of precision has been reached,
        if(poly(var) <= 10**(-1*digits) and poly(var) >= (-1*(10**(-1*digits)))):
            return var

        # The root lies in between start and end, never play outside the boundaries :p 
        assert (poly(start)*poly(end) <= 0)
    
        # check on which side our var is on towards start or end?
        if( (poly(var)<0 and poly(start)<0) or (poly(var)>0 and poly(start)>0) ):
            # its on start's side, doesnt matter wheather thats positive or negative
            # we know that the root is between var and end, the new start is
            start = var
        else:
            # then var has to lie on the other side 
            end = var
        # for debuggind and letting the user know whats happening
        #print "\nThe start,end,var is "+str(start)+" "+str(end)+" "+str(var)
        #print "The start,end,var is "+str(poly(start))+" "+str(poly(end))+" "+str(poly(var))
        print "\nThe root lies between  "+str(start)+" AND "+str(end)+" \n working... shortening the range"

while(stop == False):
    # At a root of odd multiplicity the graph of the function crosses the x-axis, whereas at a root of
    # even multiplicity the graph touches the x-axis. the first 2 methods can only deal with roots of even mutiplicity
    print "Enter 1 to find the root of a polynomial by the Bisection Method"
    print "Enter 2 to find the root of a polynomial by the Regula-Falsi"
    resp = raw_input()

    if(resp == "1"):
        # now to find the region where the function changes sign
        print "\nTo start the approximation we need to establish a region (a,b) where the root lies \nthis method can only find roots which have even multiplicity ie, the curve crosses the graph at that point  \n"
        
        while(found == False):
            # catch ValueError caused when user enters invalid a or b
            try:
                print "Enter a possible 'a'"
                a = float(raw_input())
                print "Enter a possible 'b'"
                b = float(raw_input())
            except ValueError:
                print "You have entered a Invalid value for a or b, please try again."
                continue

            if((poly(a)*poly(b)) < 0):
                print "Thank you There lies a root in this range! we shall find it."
                found = True
            else:
                print "\nSorry Please try again. use Control + C to exit the program."

        # Get the precision to which the root must be found NO NEED CAUSE WE BETTER AIM FOR SUPER PRECISION
        print "Enter the number of digits after the decimal point to which the root should be found (maximum 11)"
        digits = int(raw_input())

        ans = bisection(a,b)
        # we truncate the non-significant digits      
        print "\n\nThe root has been found to be approximately "+str(ans)[0:len(str(int(ans)))+1+digits]
    elif(resp == "2"):
        # now to find the region where the function changes sign
        print "\nTo start the approximation we need to establish a region (a,b) where the root lies \nthis method can only find roots which have even multiplicity ie, the curve crosses the graph at that point  \n"
        
        while(found == False):
            # catch ValueError caused when user enters invalid a or b
            try:
                print "Enter a possible 'a'"
                a = float(raw_input())
                print "Enter a possible 'b'"
                b = float(raw_input())
            except ValueError:
                print "You have entered a Invalid value for a or b, please try again."
                continue

            if((poly(a)*poly(b)) < 0):
                print "Thank you There lies a root in this range! we shall find it."
                found = True
            else:
                print "\nSorry Please try again. use Control + C to exit the program."

        # Get the precision to which the root must be found NO NEED CAUSE WE BETTER AIM FOR SUPER PRECISION
        print "Enter the number of digits after the decimal point to which the root should be found (maximum 11)"
        digits = int(raw_input())

        ans = regulafalsi(a,b)
        # we truncate the non-significant digits      
        print "\n\nThe root has been found to be approximately "+str(ans)[0:len(str(int(ans)))+1+digits] 
    else:
        print "You have entered a Invalid choice"

    print "Do you want to exit the program? (y/n)"
    resp2 = raw_input()
    if(resp2 == "y"):
        stop = True
    else:
        # reset the flag so that the user can look for the root in a different range
        found = False
        
        
        
