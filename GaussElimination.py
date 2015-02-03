# Gauss - Jordan Elimination Method

import sys


def storeIntoMatrix(A,n):
    print "\n Now enter the values for the "+str(n)+"x"+str(n)+" matrix"
    for row_number in range(n):
        for column_number in range(n):
            print "\nEnter the row - "+str(row_number+1)+" and column - "+str(column_number+1)+" element"
            A.append(raw_input())

def printMatrix(A,n,r):
    print "The matrix"
    for ele in range(n):
        if(ele%r == 0 and ele!=0):
            print "\n"
        sys.stdout.write( A[ele] +"\t") 

A = []
B = []
AaugB = []

print "We will solve for X in AX=B"

print "\n Enter the size of the matrix of coefficients, A"
n = int(raw_input())

storeIntoMatrix(A,n)

print "\nThe matrix A you entered was ==>"
printMatrix(A,n*n,n)

print "\nNow enter the Matrix B"
for ele in range(n):
    B.append(raw_input())

print "The equation you want to solve is as follows"

printMatrix(A,n*n,n)
print "\nMULTIPLIED BY"
for unknown in range(n):
    print "x"+str(unknown+1)
print "EQUALS"
for ele in B:
    print ele

print "\nProceeding to perform Gauss Jordan Elimination"

counter = 0
# Now we need the augmented matrix A|B so that we can start
for ele in range((n+1)*n):
    if(ele%(n+1) == 0 and ele!=0):
        AaugB.append(B[ele%(n+1)])
        counter = counter+1
        continue
    try:
        AaugB.append(A[ele-counter])
    except IndexError:
        print AaugB
printMatrix(AaugB,(n+1)*n,n+1)


