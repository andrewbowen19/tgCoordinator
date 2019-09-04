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

purpleNU = '#4E2A84'

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
	ax.hist(indExpScore, bins = 5, color = purpleNU)#histogram with Northwestern purple Go 'Cats
	ax.set_xlim((0,6))
	ax.set_ylim((0,6))
	ax.set_xlabel('Visitors\' experience scores')
	ax.set_title(guideName)

	# Route Score
	f,ax = plt.subplots(figsize = (8,5))
	ax.hist(indRouteScore, bins = 5, color = purpleNU)
	ax.set_xlim((0,6))
	ax.set_ylim((0,6))
	ax.set_xlabel('Visitors\' Route Scores')
	ax.set_title(guideName)

	# Guide Score
	f,ax = plt.subplots(figsize = (8,5))
	ax.hist(indGuideScore, bins = 5, color = purpleNU)
	ax.set_xlim((0,6))
	ax.set_ylim((0,6))
	ax.set_xlabel('Guide Score Scores')
	ax.set_title(guideName)

	# ######### Scatter plots to see score correlations ###########

	# Guide Score - Exp Score
	f,ax = plt.subplots(figsize = (8,5))
	ax.scatter(indGuideScore, indExpScore, color = purpleNU)
	ax.set_xlim((0,6))
	ax.set_ylim((0,6))
	ax.set_xlabel('Guide Score')
	ax.set_ylabel('Experience Score')
	ax.set_title(guideName)

	# route Score - Exp Score
	f,ax = plt.subplots(figsize = (8,5))
	ax.scatter(indRouteScore, indExpScore, color = purpleNU)
	ax.set_xlim(0,6)
	ax.set_ylim((0,6))
	ax.set_xlabel('Route Score')
	ax.set_ylabel('Experience Score')
	ax.set_title(guideName)

	plt.show()


# # ############################################## Interactive Part ######################################################

def NameSearch(name):
	"""fucntion to check for good names in dataframe, 
	if the names aren't present/spelled correclty, passed to retry function"""
	
	# Best case scenario
	if name in list(names):
		print('Found them!')
		# functions from above:
		makeGuidePlots(name)

		return True


	# Capitalization errors - turn everything uppercase as a c
	elif name.upper() in [x.upper() for x in list(names)]:
		print('Got \'em!')
		# Make files/plots for that individual guide's name - functions in guide-feedback
		makeGuidePlots(name)

		return True


	# Only first name used in search
	elif any(name in x for x in list(names)):

		print('Oooh thats a toughy')
		# Make files/plots here - functions in guide-feedback
		makeGuidePlots(name)

		return True

	# Bad name searched with
	else:
		return False


#While loop to keep application running until user quits
tryAgain = True
	
while tryAgain == True:

	searchType = input('Would you like to analyze the feedback for all or individual guides? (all/ind): ')
	if searchType == 'all' or searchType == 'All' or searchType == 'ALL':
		makePlots(feedback)
		tryAgain = False

	elif searchType == 'ind' or searchType == 'IND' or searchType == 'Ind':


		guideName = input('Which guide\'s feedback would you like to analyze?: ')
		search = NameSearch(guideName)

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







