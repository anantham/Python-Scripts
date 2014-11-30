# Consider an array A, of numbers. What you want to do is
# to find two points (elements) in the array such that the sum of
# all the elements between those points (including the two endpoints)
# is the maximum possible sum of any such subarray.
# ?(containing at least one positive number)
# This is termed the maximum subarray problem.

# This algorithm follows the famous method of "divide and conquer" {O(nLogn) Time}

print "Enter the number of elements in the entire Array"
no=int(raw_input())

array=[]
for i in range(0,no):
    print "Enter "+str(i+1)+"th character"
    array.append(int(raw_input()))

print "For divide and Conquer press 1 for dynamic programming press 2"
choice=int(raw_input())
# Stratagy -

# here start is the first element in the passed array,end is the last and
# mid is the middle (any of the 2 possible?? if n is even) element.
# n is the size so n=(end_index)+1

# Divide the array into 3 subarrays and find the maximum of those
# 1 - subarray containing first element as start till the mid( including it )
# 2 - subarray containing last element as end from the element after mid

# These 2 cases can be passed back to the function as recursion until the
# 3rd case is invoked.

# 3 - when the subarray is in the middle of the array such that the
#     subarray crosses the midpoint.

# Now this is where we encounter a edge case, a end point to this recursive function
# so now we need to find the maximum subarray of all sub arrays which has the
# the mid element in it.
# let this be an array with start index i and end index j,
# i>0 and i<(mid_index) and j>(mid_index) and j<(end_index)

# this will the same subarray which we will get if we find the maximum subarray
# among all subarrays which end at mid (start at some index before mid_index)
# and all subarrays which begin just after mid, ie (mid_index+1)

# thus the problem is now of finding the 2 seperate subarrays and joining them (union)
# we can find them in linear time.

# Start coding!

#   Some utility functions to find the sum of 2 or 3 integers (which we will have to do many times!)
# 2 numbers
def max2(a,b):
    if a>=b:
        # left bais - favor left argument in case of draw
        return a
    else:
        return b
# 3 numbers 
def max(a,b,c):
    return(max2(a,max2(b,c)))

# to find the max subarray in the 3rd case
# a is the array, start, mid and end are the respective array indices
def maxsubarray3(a,start,mid,end):
    # we need to find both sums of the left maxsubarray and the right maxsubarray.
    # the sum of which will be the sum of the joint subarray (from i to j) the actual max subarray of a
    # where i and j are such that,
    
    # The subarray from i to mid_index is the maximum you can get
    # from all subarrays where i which is before mid_index

    # keeps track of all the the possible subarray sums
    tempsum=0
    # keeps track of the current top sum (for the left half)
    # initially keep it as a very negative number 
    leftsum=-999999999999
    
    # lets take first half and find the maximum subarray,
    # start from mid and by decrementing ( therefore the -1 )
    # and go till the 2nd element ( therefore till array indice 1 ) 
    for i in range(mid,0,-1):
        tempsum=tempsum+a[i]
        if(tempsum>leftsum):
            # the new top sum
            leftsum=tempsum
            
    # just like how we got the leftsum, repeat for right sum.
        
    tempsum=0 
    rightsum=-999999999999

    # we now check for all possible subarrays in the right half, ie
    # mid+1 till end ( Note that the range(a,b,c) function
    # produces a list of a,a+c,a+2c,.. so on till b-1 )
    for j in range(mid+1,end+1,1):
        tempsum=tempsum+a[i]
        if(tempsum>rightsum):
            # the new top sum
            rightsum=tempsum

    # now the actualsum of the max subarray in 3rd case is returned
    return (rightsum+leftsum)

# Actual function to solve the max subarray problem
def maxsubarray(a,start,end):
    # Base case when recursion caused the array to finally become a single element
    # the element itself is the only sum, therefore the maximum
    if(start==end):
        return a[start]

    # find mid
    mid=(start+end)/2

    # now we can find the maximum of the 3 cases
    return max(maxsubarray(a,1,mid),maxsubarray(a,mid+1,end),maxsubarray3(a,1,mid,end))

               
# now to test these functions out
print "the maxsubarray has the value "+str(maxsubarray(array,0,no-1))
