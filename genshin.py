import numpy as np 
import matplotlib.pyplot as plt  
from functools import reduce
from numpy.linalg import matrix_power

N = 5000 # total number of wishes
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
	A = 0.0004 # 1/15 of 0.6%
	B = 0.0056 # 14/15 of 0.6%
	C = 0.994 # 1 - 0.6%

	for i in range(7):
		for j in range(i*90,(i+1)*90-1):
			# j is the state index in the matrix
			M[j][630+i] = B # you get some other 5 star
			M[j][637+i] = A # you get character X
			M[j][j+1] = C # you get no 5 star this pull

		# The Archon of Wishes have taken pity on you, the 90th wish or Ci90 state has only 2 paths.
		M[(i+1)*90-1][630+i] = 0.93333 # 14/15
		M[(i+1)*90-1][637+i] = 0.06666 # 1/15

		# some other 5 star character, but gotta reset pity i.e. Bi takes you to Ci1
		M[630+i][i*90] = 1
		# you are lucky! you got character X so move from Ai to C(i+1)1 but A6 is the last state so except for that
		if(i != 6):
			M[637+i][(i+1)*90] = 1

	# You stop playing when you hit A7 - character X has been maxed out
	M[643][643] = 1

	#remove connection from A0 to C11
	M[637][90] = 0
	# let A0 become the end state
	M[637][637] = 1

	k = 1

	# The probability of moving from state C01 to A7 in k steps is M^k[0][636]
	while(k<N):
		temp = matrix_power(M,k)[0][637] # A0 getting once
		prob.append(temp)
		pulls.append(k)
		k += 1

		if(k%100==0):
			print("Probability of getting character X in "+str(k)+" pulls is "+str(temp))

	fig = plt.figure()
	plt.bar(pulls, prob)
	fig.suptitle('Genshin Impact', fontsize=20)
	plt.xlabel('Number of wishes', fontsize=18)
	plt.ylabel('Probability', fontsize=16)
	plt.show()