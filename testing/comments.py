# Feedback system for the tour guide program:
# Northwestern Univeristy Office of Undergraduate Admissions
# Segal Visitor's Center
# 1841 Hinman Ave, Evanston, IL, 60201
# Author: Andrew Bowen
# License: MIT License

"""Code to filter for postivie feedback in 'comments', will integrate into our 'Search' class"""
import numpy as np
import pandas as pd
import matplotlib.pyplot
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

names = feedback['Guide Name']

# Color for plotting (NU hexcode)
# purpleNU = '#4E2A84'

# print(feedback['Comments'])


def CommentSearch():
	'''Function to call when comments are requested by user, can search for specific guide, 
		will implement with tkinter code, may want to add filter regex function'''
	guidename = input('Which guide would you like to see feedback for?: ') # Guide name to search for - will implement with tkinter interface

	# Rudimentary guide search
	if guidename in list(names):
		print('Found them!')
		viewComs = input('Would you like to see visitor comments on this guide?[y/n]: ')
		yesAnswers = ['yes', 'Yes', 'y', 'Y'] # List of possible 'acceptable 'yes' answers to inputs

		if viewComs in yesAnswers:
			
			selectedGuide = feedback.loc[names == guidename]

			print('Comments for: ' + guidename)
			print('##########################')
			print('Visitor: ', selectedGuide['Visitor Name'] + ' ', 'Visit Date/Time: ', selectedGuide['Visit Date'])
			print(selectedGuide['Comments'])
			print('##########################')

		else:
			print('Ard bet')
			pass
	# If answer 'no' or enter erroneous guide name
	else:
		print('Ight Imma head out then')
		pass

xx = CommentSearch()






















