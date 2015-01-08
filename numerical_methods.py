# This program is to implement the various methods taught in MA202 by Dr T.N.Janakiraman

# DEFINE FUNCTION IN THE CODE for now
# the polynomial is defined here
def poly(x):
    return (x-3)*(x+2)*(x+4)

found = stop = False
digits = 4
# the recursive function to find the root using Bisection Method
def bisection(start,end):
    # the coreof this function, we use 2.0 to get var as a float
    var = (start+end)/2.0
    
    # if we are lucky enough to be looking for a root
    # that can be described using a finte number of digits, and find it
    if(poly(start) == 0):
        return start
    if(poly(end) == 0):
        return end
   
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
    # SHOULD I USE RECURSION, WONT A LOOP BE FASTER? MORE EFFECTIVE
    return bisection(start,end)

while(stop == False):
    
    print "Enter 1 to find the root of a polynomial by the Bisection Method"
    print "Enter 2 to find the root of a polynomial by the Regula-Falsi"
    resp = raw_input()

    if(resp == "1"):
        # now to find the region where the function changes sign
        print "\nTo start the approximation we need to establish a region (a,b) where the root lies\n"
        
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
        print "Enter the number of digits to which the root should be found"
        digits = int(raw_input())
        
        
        print "The root has been found to be "+str(bisection(a,b))
    elif(resp == "2"):
        # do stuff here
        print "This feature is under construction"
    else:
        print "You have entered a Invalid choice"

    print "Do you want to exit the program? (y/n)"
    resp2 = raw_input()
    if(resp2 == "y"):
        stop = True
    else:
        # reset the flag so that the user can look for the root in a different range
        found = False
        
        
        
