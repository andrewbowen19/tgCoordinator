# Feedback system for the tour guide program:
# Northwestern Univeristy Office of Undergraduate Admissions
# 1841 Hinman Ave, Evanston, IL, 60201
# Author: Andrew Bowen



"""
Script for us to read in tour guide feedback and send it to the correct individual guide feedback file 
(to be posted on google drive).
Want guides to have feedback visible only to them and coordinators (from coordinator account)

"""

# Importing needed modules
import pandas as pd
import matplotlib.pyplot as plt

# Reading in visitor feedback files (responses for every guide/tour)
indpath = '/Users/andrewbowen/tgCoordinator/data/indFiles/'
allpath = '/Users/andrewbowen/tgCoordinator/data/allFiles/'
feedback = pd.read_csv(allpath + 'Feedback_Form_Beta.csv', sep = ',',header = 0)

# Renaming the columns for easier readability
feedback.columns = ['Timestamp','Visitor Name', 'Visitor Email', 'Visitor Type', 'Visit Date', 'Guide Name',\
			'Exp Score', 'Route Score', 'Guide Score', 'Comments']

# Scores for plotting later
expScore = feedback['Exp Score']
guideScore = feedback['Guide Score']
routeScore = feedback['Route Score']

names = feedback['Guide Name']


# ########################################## OLD --This is contained within our functions now #######################################################
																																					#
																																					#
																																					#
# # Want to be able to type in guide's name, pull out the correct data frame, and write that to a files 											#	
# guideName = input('Guide Name: ')																													#
# GuideFeedback = feedback.loc[names == guideName]#grabbing df with only one guide's feedback - eventually we can loop through all the Guides 		#
# indGuideFeedback = GuideFeedback.drop(labels =['Timestamp','Visitor Name', \																		#
# 	'Visitor Email'], axis=1)#Don't need visitor personal info in guide files (privacy reasons)														#
																																					#
# # replacing spaces for file name cleanliness																										#
# # guideName = guideName.replace(' ', '_')																											#
																																					#
# # Setting up individual files for each guide 																										#
# guideFile = indGuideFeedback.to_csv(newpath + guideName.replace(' ', '_') +'_feedback.csv')														#
																																					#
# ###################################################################################################################################################


indpath = '/Users/andrewbowen/tgCoordinator/data/indFiles/'#Path for individual guide files
# List of all guides --  need to input list of guide names (maybe we can just import it from a csv)
GuideList = ['Lauren Gold', 'Emily Coffee', 'Andrew Bowen', 'Mia Lennon', 'Hannah Green', 'Katie Sanderson']

# ############################################## All-guide functions ###################################################

def makePlots(DataFrame):
	'''Function to make plots for statistics of all guides together,
	 takes in our feedback DF as an input and should generate plots of the same form as the individual guide plots'''
	feedback = DataFrame
	expScore = feedback['Exp Score']
	guideScore = feedback['Guide Score']
	routeScore = feedback['Route Score']

	# Experience score
	f,ax = plt.subplots(figsize = (8,5))
	ax.hist(expScore, bins = 5, color = '#4E2A84')#histogram with Northwestern purple Go 'Cats
	ax.set_xlim((0,6))
	ax.set_ylim((0,6))
	ax.set_xlabel('Visitors\' experience scores')
	ax.set_title('All Tour Guides')

	# Route Score
	f,ax = plt.subplots(figsize = (8,5))
	ax.hist(routeScore, bins = 5, color = '#4E2A84')
	ax.set_xlim((0,6))
	ax.set_ylim((0,6))
	ax.set_xlabel('Visitors\' Route Scores')
	ax.set_title('All Tour Guides')

	# Guide Score
	f,ax = plt.subplots(figsize = (8,5))
	ax.hist(guideScore, bins = 5, color = '#4E2A84')
	ax.set_xlim((0,6))
	ax.set_ylim((0,6))
	ax.set_xlabel('Guide Score Scores')
	ax.set_title('All Tour Guides')

	# ######### Scatter plots to see score correlations ###########

	# Guide Score - Exp Score
	f,ax = plt.subplots(figsize = (8,5))
	ax.scatter(guideScore, expScore, color = '#4E2A84')
	ax.set_xlim((0,6))
	ax.set_ylim((0,6))
	ax.set_xlabel('Guide Score')
	ax.set_ylabel('Experience Score')
	ax.set_title('All Tour Guides')

	# route Score - Exp Score
	f,ax = plt.subplots(figsize = (8,5))
	ax.scatter(routeScore, expScore, color = '#4E2A84')
	ax.set_xlim((0,6))
	ax.set_ylim((0,6))
	ax.set_xlabel('Route Score')
	ax.set_ylabel('Experience Score')
	ax.set_title('All Tour Guides')

	plt.show()







# ############################################## Individual Guide functions ##################################

# Function to make individual guide file
def makeGuideFile(guideName):
	'''Fucntion to create personal .csv files for each guide'''
	guideFeedback = feedback.loc[names == guideName]
	indGuideFeedback = guideFeedback.drop(labels =['Timestamp','Visitor Name', \
		'Visitor Email'], axis=1)#Don't need visitor info in guide files (privacy reasons)
	# Writing guide data to file
	guideFile = indGuideFeedback.to_csv(indpath + guideName.replace(' ', '_') +'_feedback.csv')


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
	ax.set_ylim((0,6))
	ax.set_xlabel('Visitors\' experience scores')
	ax.set_title(guideName)

	# Route Score
	f,ax = plt.subplots(figsize = (8,5))
	ax.hist(indRouteScore, bins = 5, color = '#4E2A84')
	ax.set_xlim((0,6))
	ax.set_ylim((0,6))
	ax.set_xlabel('Visitors\' Route Scores')
	ax.set_title(guideName)

	# Guide Score
	f,ax = plt.subplots(figsize = (8,5))
	ax.hist(indGuideScore, bins = 5, color = '#4E2A84')
	ax.set_xlim((0,6))
	ax.set_ylim((0,6))
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


# ############################################## Interactive Part ######################################################

query = input('Would you like to see all-guide feedback or individual guide feedback?:(all/ind) ')

if query == 'all' or query == 'ALL' or query == 'All':
	makePlots(feedback)
	# print('Data table for all guides: ',feedback)

elif query == 'ind'or query == 'IND' or query == 'Ind' or query == 'Individual':
	guideName = input('Guide Name: ')

	if guideName in GuideList:
		makeGuideFile(guideName)

		plotsQuery = input('Would you like to see graphs of this guide\'s responses? (yes/no): ')
		if plotsQuery == 'yes' or plotsQuery == 'y':
			makeGuidePlots(guideName)

	# Want to check for lowercase/incomplete spellings with this condition
	elif any(guideName in x for x in GuideList):

		newGuideName = guideName.capitalize()
		makeGuideFile(newGuideName)
		makeGuidePlots(newGuideName)

	else:
		print('That name is not in our guide database, please double check spelling.')




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








