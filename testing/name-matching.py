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

import numpy as np

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

def randomScat():
	"""Test plotting function for us to use as a placeholder"""
	x = np.random.random(100)
	y = np.random.random(100)

	f,ax = plt.subplots()
	ax.scatter(x,y)
	ax.set_xlabel('x')
	ax.set_ylabel('y')
	ax.set_title('TEST PLOT')
	plt.show()

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

# def NameSearch():
# 	'''
# 	Function for us to integrate with our guide-feedback script, looks to aid in name matching for user 
# 	and correct for spelling errors in database, because parents will often give incomplete/oncorrectly spelled names
# 	'''


# 	tryAgain = True

# 	def goodNames(name):
# 		"""Nested fucntion to check for good names in dataframe, 
# 		if the names aren't present/spelled correclty, passed to retry function"""
	
# 		# Best case scenario
# 		if name in list(rawNames):
# 			print('Found them!')
# 			# make files/plots as needed (can insert into our other code guide-feedback)
# 			randomScat()
# 			return True


# 		# Capitalization errors - turn everything uppercase as a c
# 		elif name.upper() in [x.upper() for x in list(rawNames)]:
# 			print('Got \'em!')
# 			# Make files/plots for that individual guide's name
# 			randomScat()
# 			return True


# 		# Only first name used in search
# 		elif any(name in x for x in list(rawNames)):

# 			# print(any(name in x for x in list(rawNames)))

# 			print('Oooh thats a toughy')
# 			# Make files/plots here
# 			randomScat()
# 			return True

# 		# Bad name searched with
# 		else:
# 			return False

# 	def doItAgain():
# 		'''Function for us to call if goodNames fails (name not listed), 
# 		checks if user wants to search again, if they do, runs goodNames again. If not, kills the application'''

# 		################ This section not working
# 		newSearch = input('Would you like to try again? (yes/no): ')

# 		if newSearch == 'yes' or newSearch == 'y':
# 			newName = input('Guide Name: ')
# 			goodNames(newName)
# 			return True

# 		elif newSearch == 'no' or newSearch == 'n' or newSearch == 'No' or newSearch == 'NO':
# 			return False

# 	searchName = input('Which guide\'s feedback would you like to analyze?: ')		
# 	# search = goodNames(searchName)




# 	# # While loop to keep program running until user quits
# 	while tryAgain == True:
# 		search = goodNames(searchName)#running search for good user input names

# 		# If name was successfully recovered
# 		if search == True:
# 			SearchAgain = input('Would you like to analyze the feedback for another guide? (yes/no): ')

# 			if SearchAgain == 'yes' or SearchAgain == 'y':
# 				newName = input('Guide Name: ')
# 				goodNames(newName)
	

# 			#User doesn't want to keep searching, kills application 
# 			elif SearchAgain == 'no' or SearchAgain == 'n':
# 				tryAgain = False


# 		# If second search is bad, try again (unless they don't want to)
# 		elif search == False:
# 			print('That guide is not in out database. foo foo')
# 			again = doItAgain()	

# 			# Kills app
# 			if again == False:
# 				tryAgain = False
# 	return None




# Almost ready to integrate with guide-feedback script ---- needs some user debugging!!!


# CoordQuery = NameSearch()

# #########################################

def goodNames(name):
	"""fucntion to check for good names in dataframe, 
	if the names aren't present/spelled correclty, passed to retry function"""
	
	# Best case scenario
	if name in list(rawNames):
		print('Found them!')
		# make files/plots as needed (can insert into our other code guide-feedback)
		randomScat()
		return True


	# Capitalization errors - turn everything uppercase as a c
	elif name.upper() in [x.upper() for x in list(rawNames)]:
		print('Got \'em!')
		# Make files/plots for that individual guide's name
		randomScat()
		return True


	# Only first name used in search
	elif any(name in x for x in list(rawNames)):

		print('Oooh thats a toughy')
		# Make files/plots here
		randomScat()
		return True

	# Bad name searched with
	else:
		return False


# ############################## Run again function -- do not use!!!! ############################################
# def doItAgain():
# 	'''Function for us to call if goodNames fails (name not listed), 
# 	checks if user wants to search again, if they do, runs goodNames again. If not, kills the application'''

# 	################ This section not working
# 	newSearch = input('Would you like to try again? (yes/no): ')

# 	if newSearch == 'yes' or newSearch == 'y':
# 		newName = input('Guide Name: ')
# 		goodNames(newName)
# 		return True

# 	elif newSearch == 'no' or newSearch == 'n' or newSearch == 'No' or newSearch == 'NO':
		# return False

#While loop to keep application running until user quits
tryAgain = True
	
while tryAgain == True:
	guideName = input('Which guide\'s feedback would you like to analyze?: ')
	search = goodNames(guideName)

	# If output of goodnames function is True
	if search == True:
		newSearch = input('Would you like to analyze the feedback of another guide? (y/n): ')

		# User wants to search more guides
		if newSearch == 'y' or newSearch == 'yes':
			tryAgain = True

		# Kills app
		elif newSearch == 'n' or newSearch == 'no':
			tryAgain = False

	# User searched a bad name - misspelled or otherwise
	elif search == False:
		print('That guide is not in our database.')

		# Asks to search again
		newSearch = input('Would you like to analyze the feedback of another guide? (y/n): ')

		# User can search more guides
		if newSearch == 'y' or newSearch == 'yes':
			tryAgain = True

		# Kills app
		elif newSearch == 'n' or newSearch == 'no':
			tryAgain = False










