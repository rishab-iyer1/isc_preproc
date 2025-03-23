#!/usr/bin/env python3

import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

def feeling_trend(boundaries,title):
	df = pd.read_excel('/Volumes/BCI/Ambivalent_Affect/Label_Aggregate.xlsx', skiprows=2)
	
	
	# Compute the percentage of subjects in each state at each time point
	total_counts = df.count(axis=1)
	P_counts = df[df == 'P'].count(axis=1)
	N_counts = df[df == 'N'].count(axis=1)
	M_counts = df[df == 'M'].count(axis=1)
	X_counts = df[df == 'X'].count(axis=1)
	
	total_counts = P_counts + N_counts + M_counts + X_counts
	
	P_percentage = (P_counts / total_counts) * 100
	N_percentage = (N_counts / total_counts) * 100
	M_percentage = (M_counts / total_counts) * 100
	X_percentage = (X_counts / total_counts) * 100
	
	window_size = 10 # in samples
	P_percentage_smoothed = P_percentage.rolling(window_size, center=True).mean()
	N_percentage_smoothed = N_percentage.rolling(window_size, center=True).mean()
	M_percentage_smoothed = M_percentage.rolling(window_size, center=True).mean()
	X_percentage_smoothed = X_percentage.rolling(window_size, center=True).mean()
	
	plt.figure(figsize=(14,8))
	plt.plot(P_percentage_smoothed, color='red')
	plt.plot(N_percentage_smoothed, color='blue')
	plt.plot(M_percentage_smoothed, color='purple')
	plt.plot(X_percentage_smoothed, color='dimgrey')
	plt.xticks(np.arange(0, 460, 20))

	# for i in range(len(boundaries)):
		# plt.axvline(boundaries[i],color='black')
	
	plt.xlabel('Time')
	plt.title(title)
	plt.ylabel('Percentage of subjects')
	plt.legend(['Positive', 'Negative', 'Mixed', 'Neutral'])
	fig_title = '/Volumes/BCI/Ambivalent_Affect/fMRI_Study/Group_Analyses/' + title + '.png'
	plt.savefig(fig_title)
	plt.show()


def feeling_probability():
	import pandas as pd
	import numpy as np

	# Read in the CSV file
	df = pd.read_excel('/Users/anthonyvaccaro/Label_Aggregate.xlsx', skiprows=2)

	# Remove the first column (subject IDs)
	df = df.iloc[:, 1:]

	# Drop rows with NaN values
	df = df.dropna()

	# Define the states
	states = ['P', 'N', 'X', 'M']

	# Calculate the transition probability matrix for each subject
	subject_prob_matrices = {}
	for subject in range(len(df.columns)):
	    # Initialize the probability matrix
	    prob_matrix = pd.DataFrame(np.zeros((len(states), len(states))), index=states, columns=states)

	    # Iterate through each time point
	    for i in range(1, len(df)):
	        # Get the current state and the previous state
	        curr_state = df.iloc[i, subject]
	        prev_state = df.iloc[i-1, subject]

	        # Increment the corresponding transition probability in the matrix
	        prob_matrix[curr_state][prev_state] += 1

	    # Normalize the matrix to get transition probabilities
	    prob_matrix = prob_matrix.div(prob_matrix.sum(axis=1), axis=0)

	    # Add the matrix to the dictionary of subject probability matrices
	    subject_prob_matrices[subject] = prob_matrix

	# Calculate the overall transition probability matrix
	overall_prob_matrix = pd.DataFrame(np.zeros((len(states), len(states))), index=states, columns=states)
	for subject in range(len(df.columns)):
	    overall_prob_matrix += subject_prob_matrices[subject]

	overall_prob_matrix = overall_prob_matrix.div(overall_prob_matrix.sum(axis=1), axis=0) 
	print(overall_prob_matrix)
