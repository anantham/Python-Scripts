# Gaussian Elimination, Gauss Jordan  - Methods

import sys

A = []
B = []
AaugB = []
number_of_variables = 0

# stores a nxm martix in A as a nested list, A will be a list containing n lists (rows) each with m elements (columns)
def storeIntoMatrix(A,n,m):
    print "\n Now enter the values for the " + str(n) + "x" + str(m) + " matrix"
    for row_number in range(n):
        temp_row = []
        for element_number in range(m):
            print "\n Enter the row - " + str(row_number+1) + " and column - " + str(element_number+1) + " element"
            temp_row.append(raw_input())
        A.append(temp_row)

def printMatrix(A):
    for row in A:
    	for element in row:
    		sys.stdout.write( "\t" + element + "\t")
    	print "\n"

def handle_row(M,pivot_row,row_number,multiplication_factor,row_size):
	print "\n Handling row "+str(row_number+1)+" with pivot from row "+str(pivot_row+1)+"\n"
	for element_number in range(row_size):
		M[row_number][element_number] = str( float(M[row_number][element_number]) - float(M[pivot_row][element_number]) * multiplication_factor)
	printMatrix(M)

def MakeUpperTriangular(M,n,m):
	# each iteration of this loop handles the case where the pivot exists in that row
	for pivot_row in range(n):
		# the diagonal element is the pivot
		pivot = M[pivot_row][pivot_row]
		# now we use this pivot to make all elements below the pivot in column 'row_number' zero
		# ie the elements M[i][row_number] where i E (row_number,n-1)
		for below_row in range(pivot_row+1,n):
			if(float(pivot) == 0):
				print "Matrix is Singular"
				return
			multiplication_factor = float(M[below_row][pivot_row])/float(pivot)
			handle_row(M,pivot_row,below_row,multiplication_factor,m)

def SetUpMatrices():
	print "\n Enter the size of the matrix of coefficients, A. \n This 'n' will be the number of variables in X"
	n = int(raw_input())

	storeIntoMatrix(A,n,n)

	print "\n The matrix A you entered was ==> \n"
	printMatrix(A)

	print "\nNow enter the column Matrix B"
	for element_number in range(n):
		print "\n Enter "+str(element_number+1)+"th element"
		B.append(raw_input())

	return n


print "\n Welcome to my program, here we will solve for X \n in the equation AX = B using various methods"

number_of_variables = SetUpMatrices()

# generate AaugB
i = 0
for row in A:
	temp_row=row
	temp_row.append(B[i])
	AaugB.append(temp_row)
	i = i + 1

print "\n\n The equation AX = B is as follows \n"
printMatrix(A)
print "\n     MULTIPLIED BY\n"
for unknown_no in range(number_of_variables):
    print "        X"+str(unknown_no+1)
print "\n     EQUALS\n"
for element in B:
    print "        "+str(element)

# Partial Pivoting in order to handle it if the equations are supplied in wrong order!!
print "\n Start partial pivoting\n"
for column_number in range(number_of_variables):
	temp_row = []
	for element in range(number_of_variables):
		temp_row.append(float(AaugB[column_number][element]))
	pivot_row = temp_row.index(max(temp_row))
	if(pivot_row == column_number):
		print " no need to shift the row for pivot number"+str(column_number+1)
		break
	print "\n shift row no "+str(pivot_row)+" to the pivot row number "+str(column_number)+"\n"
	temp = AaugB[pivot_row]
	AaugB[pivot_row] = AaugB [column_number]
	AaugB[column_number] = temp
	printMatrix(AaugB)

# FORWARD ELIMINATION
MakeUpperTriangular(AaugB,number_of_variables,number_of_variables+1)

# we have the matrix A in row - echelon form


