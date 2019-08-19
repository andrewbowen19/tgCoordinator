# Feedback system for the tour guide program:
# Northwestern Univeristy Office of Undergraduate Admissions
# 1841 Hinman Ave, Evanston, IL, 60201
# Author: Andrew Bowen


"""
Test script to match names from visitor input - will likely only give first names (often misspelled)
"""

import pandas as pd
import matplotlib.pyplot as plt
import re


# Reading in data files (all guide feedback)
indpath = '/Users/andrewbowen/tgCoordinator/data/indFiles/'
allpath = '/Users/andrewbowen/tgCoordinator/data/allFiles/'
feedback = pd.read_csv(allpath + 'Feedback_Form_Beta.csv', sep = ',', header = 0)

# Renaming the columns for easier readability
feedback.columns = ['Timestamp','Visitor Name', 'Visitor Email', 'Visitor Type', 'Visit Date', 'Guide Name',\
			'Exp Score', 'Route Score', 'Guide Score', 'Comments']


# raw input names from visitors - will likely have spelling errors/only first names
rawNames = feedback['Guide Name']

# Checking if capitalize/upper string method works
# for n in list(rawNames):
# 	c = n.upper()
# 	print(c)


# ###############################################################################################################################

# PSEUDO CODE
# input guideName #asks for guides name from user
# if guideName is in rawNames (maybe make it a list/np array):
	# run stuff
# elif guideName is in list but not capitalized properly
	# capitalize name string to match list value

# Elif only first name given
	# input (guide last name)
# 	Maybe correlate this to time given/have a guide dictionary of tour times given (payroll csv maybe?) - check Humanity
# 
# Also we're assuming the name we search the database with is correctly spelled/capitalized
# ################################################################################################################################


# Function for us to do a name search, should be easier to keep running

def NameSearch():
	# Input from the user to search for an individual guide
	searchName = input('Which guide\'s feedback would you like to analyze?: ')

	# Best case scenario
	if searchName in list(rawNames):
		print('Found them!')
		# make files/plots as needed (can insert into our other code guide-feedback)

	# Capitalization errors - turn everything uppercase as a c
	elif searchName.upper() in [x.upper() for x in list(rawNames)]:
		print('Got \'em!')
		# Make files/plots for that individual guide's name


	# Only first name
	elif any(searchName in x for x in list(rawNames)):#If the query name is contained in the rawNames list (only search with a first name)
		# There are more than one Andrew
		print(any(searchName in x for x in list(rawNames)))

		print('Oooh thats a toughy')

	# Bad guide name
	else:
		print('That guide is not in our database.')

		newSearch = input(' Would you like to try again? (yes/no):')

		if newSearch == 'y' or newSearch == 'yes':
			# NameSearch() - can call in general script


	# I'd be interested to see if there is a way to keep this input running even if the answer is wrong



# Almost ready to integrate with guide-feedback script


CoordQuery = NameSearch()






