import numpy as np 
import matplotlib.pyplot as plt  
from functools import reduce
from numpy.linalg import matrix_power

N = 2000 # total number of wishes
pulls = []
prob = []

# Build the transition matrix of size 7+7+90*7 = 644*644
M = np.zeros((644,644))

def wander():
	# TODO fix overestimation of wishes because transition states A and B are also being counted as a wish right now.

	# states 0*90 = 0 	 to 1*90-1  = 89  are C01 to C090, 
	# states 1*90 = 90   to 2*90-1  = 179 are C11 to C190,
	# states 2*90 = 180  to 3*90-1  = 269 are C21 to C290, 
	# states 3*90 = 270  to 4*90-1  = 359 are C31 to C390,
	# states 4*90 = 360  to 5*90-1  = 449 are C41 to C490, 
	# states 5*90 = 450  to 6*90-1  = 539 are C51 to C590,
	# states 6*90 = 540  to 7*90-1  = 629 are C61 to C690,
	# states 630         to 630+7-1 = 636 are B0 to B6
	# states 637         to 637+7-1 = 643 are A0 to A6

	# There are only 3 paths out of states Cij; to Ai, Bi or Ci(j+1) for j in 1 to 89, 
	# the 90th consecutive NON 5 star pull will take you to a 5 star state, either A or B
	A = 0.003 # 1/15 of 0.6%
	B = 0.003 # 14/15 of 0.6%
	C = 0.994 # 1 - 0.6%

	# set up connections only for first section of states
	for i in range(1):
		for j in range(i*90,(i+1)*90-1):
			# j is the state index in the matrix
			M[j][630+i] = B # you get some other 5 star
			M[j][637+i] = A # you get character X
			M[j][j+1] = C # you get no 5 star this pull

		# The Archon of Wishes have taken pity on you, the 90th wish or Ci90 state has only 2 paths.
		M[(i+1)*90-1][630+i] = 0.5 # 14/15
		M[(i+1)*90-1][637+i] = 0.5 # 1/15


	# let A0 take you to C21 (I am using C1j to keep track of 180 pity)
	M[637][180] = 1

	# set B0 to C11 and let that set of 90 pulls lead to klee for sure
	M[630][90] = 1 # if first 90 pity fails to get klee move to C11

	# Assign probabilities for C1j states
	for j in range(90,179):
		M[j][637] = A+B # you get klee for sure
		M[j][j+1] = C # you get no 5 star this pull

	M[179][637] = 1 # 180 pity gets you klee for sure, no need to use A1 or B1

	for i in range(2,7):
		for j in range(i*90,(i+1)*90-1):
			# j is the state index in the matrix
			M[j][630+i] = B # you get some other 5 star
			M[j][637+i] = A # you get character X
			M[j][j+1] = C # you get no 5 star this pull

		# The Archon of Wishes have taken pity on you, the 90th wish or Ci90 state has only 2 paths.
		M[(i+1)*90-1][630+i] = 0.5 
		M[(i+1)*90-1][637+i] = 0.5
		
		M[630+i][i*90] = 1
		if(i != 6):
			M[637+i][(i+1)*90] = 1

	M[643][643] = 1

	k = 1

	# The probability of moving from state C01 to A7 in k steps is M^k[0][636]
	while(k<N):
		temp = matrix_power(M,k)[0][643] # A0 getting once
		prob.append(temp)
		pulls.append(k)
		k += 1

		if(k%10==0):
			print("Probability of getting character X in "+str(k)+" pulls is "+str(temp))

	fig = plt.figure()
	plt.bar(pulls, prob)
	fig.suptitle('Genshin Impact', fontsize=20)
	plt.xlabel('Number of wishes', fontsize=18)
	plt.ylabel('Probability', fontsize=16)
	plt.show()