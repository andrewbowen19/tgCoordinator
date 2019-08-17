# Feedback system for the tour guide program:
# Northwestern Univeristy Office of Undergraduate Admissions
# 1841 Hinman Ave, Evanston, IL, 60201
# Author: Andrew Bowen



"""
Script for us to read in TG feedback and send it to the correct TG feedback file 
(to be posted on google drive).
Want guides to have feedback visible only to them and coordinators (from coordinator account)

"""

# Importing needed modules
import pandas as pd
import matplotlib.pyplot as plt

# Reading in visitor feedback files (responses for every guide/tour)
path = '/Users/andrewbowen/tgCoordinator/'
feedback = pd.read_csv(path + 'Feedback_Form_Beta.csv', sep = ',',header = 0)

# Renaming the columns for easier readability
feedback.columns = ['Timestamp','Visitor Name', 'Visitor Email', 'Visitor Type', 'Visit Date', 'Guide Name',\
			'Exp Score', 'Route Score', 'Guide Score', 'Comments']

# Scores for plotting later
expScore = feedback['Exp Score']
guideScore = feedback['Guide Score']
routeScore = feedback['Route Score']

names = feedback['Guide Name']

# Want to be able to type in guide's name, pull out the correct data frame, and write that to a file
guideName = input('Guide Name: ')
GuideFeedback = feedback.loc[names == guideName]#grabbing df with only one guide's feedback - eventually we can loop through all the guides
indGuideFeedback = GuideFeedback.drop(labels =['Timestamp','Visitor Name', \
	'Visitor Email', 'Visitor Type', 'Visit Date'], axis=1)#Don't need visitor info in guide files (privacy reasons)

# replacing spaces for file name cleanliness
# guideName = guideName.replace(' ', '_')

# Setting up individual files for each guide
newpath = '/Users/andrewbowen/tgCoordinator/indFiles/'
guideFile = indGuideFeedback.to_csv(newpath + guideName.replace(' ', '_') +'_feedback.csv')

# List of guide names eventually to loop through, will make files for each one
# GuideList = [#FILL WITH GUIDE NAMES] - could read in from separate file

GuideList = ['Lauren Gold', 'Emily Coffee', 'Andrew Bowen', 'Mia Lennon']


# ##############################################Functions to apply to every guide ##################################

# Function to make individual guide file
def makeGuideFile(guideName):
	'''Fucntion to create personal .csv files for each guide'''
	guideFeedback = feedback.loc[names == guideName]
	indGuideFeedback = guideFeedback.drop(labels =['Timestamp','Visitor Name', \
		'Visitor Email', 'Visitor Type', 'Visit Date'], axis=1)#Don't need visitor info in guide files (privacy reasons)
	# Writing guide data to file
	guideFile = indGuideFeedback.to_csv(newpath + guideName.replace(' ', '_') +'_feedback.csv')


# function make guide plots
def makeGuidePlots(guideName):
	"""Function to make individual guide plots (exp score, route score, guide score"""
	guideFeedback = feedback.loc[names == guideName]
	indGuideFeedback = guideFeedback.drop(labels =['Timestamp','Visitor Name', \
		'Visitor Email', 'Visitor Type', 'Visit Date'], axis=1)

	indExpScore = indGuideFeedback['Exp Score']
	indGuideScore = indGuideFeedback['Guide Score']
	indRouteScore = indGuideFeedback['Route Score']
	# print(indExpScore, indGuideScore, indRouteScore)
	# Plotting
	# Experience score
	f,ax = plt.subplots(figsize = (8,5))
	ax.hist(indExpScore, bins = 5, color = '#4E2A84')#histogram with Northwestern purple Go 'Cats
	ax.set_xlim((0,6))
	ax.set_xlabel('Visitors\' experience scores')
	ax.set_title(guideName)

	# Route Score
	f,ax = plt.subplots(figsize = (8,5))
	ax.hist(indRouteScore, bins = 5, color = '#4E2A84')
	ax.set_xlim((0,6))
	ax.set_xlabel('Visitors\' Route Scores')
	ax.set_title(guideName)

	# Guide Score
	f,ax = plt.subplots(figsize = (8,5))
	ax.hist(indGuideScore, bins = 5, color = '#4E2A84')
	ax.set_xlim((0,6))
	ax.set_xlabel('Guide Score Scores')
	ax.set_title(guideName)

	# ######### Scatter plots to see score correlations ###########

	# Guide Score - Exp Score
	f,ax = plt.subplots(figsize = (8,5))
	ax.scatter(indGuideScore, indExpScore, color = '#4E2A84')
	ax.set_xlim((0,6))
	ax.set_ylim((0,6))
	ax.set_xlabel('Guide Score')
	ax.set_ylabel('Experience Score')
	ax.set_title(guideName)

	# route Score - Exp Score
	f,ax = plt.subplots(figsize = (8,5))
	ax.scatter(indRouteScore, indExpScore, color = '#4E2A84')
	ax.set_xlim(0,6)
	ax.set_ylim((0,6))
	ax.set_xlabel('Route Score')
	ax.set_ylabel('Experience Score')
	ax.set_title(guideName)

	plt.show()



# If inputted guide name is in list
if guideName in GuideList:
	makeGuideFile(guideName)
	makeGuidePlots(guideName)

else:
	print('Name not in our guide list, please double check spelling.')

	# Function should write the files automatically


# ##################################################### Visualization ######################################################

# Can create histograms of scores if we want to analyze the data
# Example below is a test case for one guide (not from 'if' statement)

# Experience score
# f,ax = plt.subplots(figsize = (8,5))
# ax.hist(expScore, bins = 5, color = '#4E2A84')#histogram with Northwestern purple Go 'Cats
# ax.set_xlabel('Visitors\' experience scores')
# ax.set_title(guideName)

# # Route Score
# f,ax = plt.subplots(figsize = (8,5))
# ax.hist(routeScore, bins = 5, color = '#4E2A84')
# ax.set_xlabel('Visitors\' Route Scores')
# ax.set_title(guideName)

# # Guide Score
# f,ax = plt.subplots(figsize = (8,5))
# ax.hist(guideScore, bins = 5, color = '#4E2A84')
# ax.set_xlabel('Guide Score Scores')
# ax.set_title(guideName)

# # ######### Scatter plots to see score correlations ###########

# # Guide Score - Exp Score
# f,ax = plt.subplots(figsize = (8,5))
# ax.scatter(guideScore, expScore, color = '#4E2A84')
# ax.set_xlabel('Guide Score')
# ax.set_ylabel('Experience Score')
# ax.set_title(guideName)

# # route Score - Exp Score
# f,ax = plt.subplots(figsize = (8,5))
# ax.scatter(routeScore, expScore, color = '#4E2A84')
# ax.set_xlabel('Route Score')
# ax.set_ylabel('Experience Score')
# ax.set_title(guideName)

# plt.show()








