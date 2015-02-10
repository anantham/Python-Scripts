# Sorting of numbers 
# we will stick to acending - read it backwards otherwise :P

def InsertionSort(A):
    # As A[0] is sorted by itself we need to take the number to be sorted from 1 to n-1
    for i in range(1,len(A)):
        key = A[i]  # Take the next number in unsorted section
        for j in range(0,i):  # go through the sorted numbers
            if(key<A[j]):
                A.insert(j,key) # COPY "key" into the right spot
                A.pop(i+1)  # remove "key" from its initial position
                break
            
response = 1
while(response == 1):
    print "Enter how many numbers are to be sorted"
    n = int(raw_input())

    A = []

    print "Enter the "+str(n)+" numbers :-"
    for i in range(n):
        A.append(float(raw_input()))

    print "Enter 1 for Insertion Sort"
    choice = int(raw_input())

    if(choice == 1):
        print "Executing insertion sort on the following numbers"
        print A
        InsertionSort(A)
        print "The sorted numbers are"
        print A
    else:
        print "invalid option"

    print "enter 1 for trying with a different set of numbers"
    response = int(raw_input())

print "thanks for using my program"
    
