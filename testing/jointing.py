# Tour Guide Program : Feedback system
# Northwestern Univeristy Office of Undergraduate Admissions
# Segal Visitors' Center
# 1841 Hinman Ave, Evanston, IL, 60201
# Author: Andrew Bowen
# License: MIT License

"""Script to test out joint-pairing efficiency, joint plots"""

import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

# Reading in visitor feedback files (responses for every guide/tour)
indpath = '/Users/andrewbowen/tgCoordinator/data/indFiles/'
allpath = '/Users/andrewbowen/tgCoordinator/data/allFiles/'
feedback = pd.read_csv(allpath + 'Feedback_Form_Beta.csv', sep = ',', header = 0)

# Renaming the columns for easier readability
feedback.columns = ['Timestamp','Visitor Name', 'Visitor Email', 'Visitor Type', 'Visit Date', 'Guide Name',\
			'Exp Score', 'Route Score', 'Guide Score', 'Comments']

# Scores for plotting later
expScore = feedback['Exp Score']
guideScore = feedback['Guide Score']
routeScore = feedback['Route Score']
names = feedback['Guide Name']#Pandas series of guide names

# print(feedback)
def makePlots(Guide1, Guide2):
	"""Function to call later to make joint par plots"""
	guide1Data = feedback.loc[feedback['Guide Name'] == Guide1]
	guide2Data = feedback.loc[feedback['Guide Name'] == Guide2]

	# Guide - Exp Score plot
	f,ax = plt.subplots()
	ax.scatter(guide1Data['Guide Score'], guide1Data['Exp Score'], color = '#4E2A84',marker = '^',label = Guide1) # Guide 1 guide-exp score
	ax.scatter(guide2Data['Guide Score'], guide2Data['Exp Score'], color = '#4E2A84',marker = 'o',label = Guide2)
	ax.set_xlim(0.,5.5)
	ax.set_ylim(0.,5.5)
	ax.set_xlabel('Guide Score')
	ax.set_ylabel('Experience Score')
	ax.set_title(Guide1 + ' ' + Guide2)
	ax.legend()

	f,ax = plt.subplots()
	ax.scatter(guide1Data['Route Score'], guide1Data['Exp Score'],  color = '#4E2A84',marker = '^',label = Guide1) # Guide 1 guide-exp score
	ax.scatter(guide2Data['Route Score'], guide2Data['Exp Score'],  color = '#4E2A84',marker = 'o',label = Guide2)
	ax.set_xlim(0.,5.5)
	ax.set_ylim(0.,5.5)
	ax.set_xlabel('Route Score')
	ax.set_ylabel('Experience Score')
	ax.set_title(Guide1 + ' ' + Guide2)
	ax.legend()

	plt.show()


def pairSearch():
	searchType = input('Would you like to search a joint pair of guides?[y/n]: ')
	if 'y' in searchType:

		name1 = input('Guide 1 Name: ')
		name2 = input('Guide 2 Name: ')
		Timestamp = feedback['Timestamp']

		guidetime1 = Timestamp.loc[names == name1]
		guidetime2 = Timestamp.loc[names == name2]

		guideName1 = feedback.loc[names == name1]
		guideName2 = feedback.loc[names == name2]

		# If timestamps are the same, they should be considered a joint pairing
		pairName = guideName1 + guideName2
		print(pairName)


		# Insert makePlots() here
		makePlots(name1, name2)

		return guidetime1, guidetime2

		# Kill function if the user inputs 'no'
	else: 
		print('Goodbye...')
		pass

			

	




# xx = makePlots('Andrew Bowen', 'Lauren Gold')
yy = pairSearch()


# pair = input('Which joint tour pair would you like to search?: ')

# print(pairSearch())










