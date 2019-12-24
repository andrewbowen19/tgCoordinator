# Feedback system for the tour guide program:
# Northwestern Univeristy Office of Undergraduate Admissions
# Segal Visitor's Center
# 1841 Hinman Ave, Evanston, IL, 60201
# Author: Andrew Bowen
# License: MIT License

'''
Script to create popup window for our guide name-entry feedback system
uses Tkinter python package to create popup windows


'''

# Source code for some of this: https://www.python-course.eu/tkinter_entry_widgets.php
# Check for any easier means ofdoing this (maybe there's some method in JavaScript?)
# import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import tkinter as tk
# Ussing themed tkinter widgets (ttk) to create more modern-looking GUIs, need to do some research on it
from tkinter.ttk import *

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
purpleNU = '#4E2A84'
greyNU = '#716C6B'

# ################################################### Writing this as a class ####################################

class Search(object):

	def __init__(self):
		self.name = None

##### Plots function from guide-feedback #######
	def makePlots(self):

		'''Function to make plots for statistics of all guides together,
		 takes in our feedback DF as an input and should generate plots of the same form as the individual guide plots

		Will not want to incorporate this for all guides (or maybe only a distilled version of it)
		Guides should only be able to see their own feedback
		 '''

		import matplotlib.pyplot as plt
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
		ax.set_xlabel('Guide Scores')
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

	######################################## Individual Guides ##############################

	def guideSearch(self):
		"""Function for widget that searches for individual guide, called after searchType"""
		self.master = tk.Tk()

		tk.Label(self.master, text="First Name").grid(row=0)
		tk.Label(self.master, text="Last Name").grid(row=1)

		self.e1 = tk.Entry(self.master)
		self.e2 = tk.Entry(self.master)
		self.e3 = tk.Entry(self.master)

		self.firstName = self.e1.grid(row=0, column=1)
		self.lastName = self.e2.grid(row=1, column=1)



		# Makes entry input
		def show_entry_fields():
			"""Function to call for our buttons when a guide's name is searched"""

			print("First Name: %s\nLast Name: %s" % (self.e1.get(), self.e2.get()))


		def makeGuidePlots():
			"""Function to make individual guide plots (exp score, route score, guide score
				Copied from our guide-feedback script in parent repo"""
			import matplotlib.pyplot as plt

			guideName = self.e1.get() + ' ' +  self.e2.get()
			guideFeedback = feedback.loc[names == guideName]
			indGuideFeedback = guideFeedback.drop(labels =['Timestamp','Visitor Name', \
				'Visitor Email', 'Visitor Type', 'Visit Date'], axis=1)

			indExpScore = indGuideFeedback['Exp Score']
			indGuideScore = indGuideFeedback['Guide Score']
			indRouteScore = indGuideFeedback['Route Score']

			# Checking guide name spelling
			# if guideName in names:

			print(guideName)

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
			ax.set_xlabel('Guide Score')
			ax.set_title(guideName)

			# ######### Scatter plots to see score correlations between scoring techniques###########

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

			# Bad search terms (misspelled guides name/not a guide)
			# else:

			# 	self.newMaster = tk.Tk()
			# 	tk.Label(self.newMaster, text="That guide is not in our database, please try again").grid(row=0)#Raises error widget
				# print('That guide is not in our database!, please try again')

		# Setting up input buttons on entry widget
		quitButton = tk.Button(self.master, text='Quit', command= self.master.quit).grid(row=3, column=0, sticky=tk.W, pady=4)#Quit button
		backButton = tk.Button(self.master, text = 'Back', command = self.master.quit).grid(row=3, column =1, sticky=tk.W, padx = 5,pady=5)#Back button
		plotsButton = tk.Button(self.master, text='View Feedback', command = makeGuidePlots).grid(row=3, column=1, sticky=tk.W, padx = 5,pady=5)#Plots button

		# Works for now, will need to add name spelling checks (or could clean that up before adding names to our db)

	def pairSearch(self):
		"""Joint pair search capability, for if we want to see how joint pairs are doing together"""
		"""Function for widget that searches for individual guide, called after searchType"""
		self.master = tk.Tk()

		tk.Label(self.master, text="Guide 1 Name:").grid(row=0)
		tk.Label(self.master, text="Guide 2 Name:").grid(row=1)

		self.e1 = tk.Entry(self.master)
		self.e2 = tk.Entry(self.master)
		self.e3 = tk.Entry(self.master)

		self.jointName1 = self.e1.grid(row=0, column=1)
		self.jointName2 = self.e2.grid(row=1, column=1)

		def jointPlots():
			"""Similar to makeGuidePlots above, but for joint pair
				We probably cna integrate these both better"""
			import matplotlib.pyplot as plt
			# plt.style.use('dark_background') # Dark themed plots from matplotlib - can use if we want, I think it's pretty cool

			guideName1 = self.e1.get()
			guideName2 = self.e2.get()
			guide1Feedback = feedback.loc[names == guideName1]
			guide2Feedback = feedback.loc[names == guideName2]
			indGuide1Feedback = guide1Feedback.drop(labels =['Timestamp','Visitor Name', \
				'Visitor Email', 'Visitor Type', 'Visit Date'], axis=1)
			indGuide2Feedback = guide2Feedback.drop(labels =['Timestamp','Visitor Name', \
				'Visitor Email', 'Visitor Type', 'Visit Date'], axis=1)

			# Guide 1 scores for plotting
			indExpScore1 = indGuide1Feedback['Exp Score']
			indGuideScore1 = indGuide1Feedback['Guide Score']
			indRouteScore1 = indGuide1Feedback['Route Score']

			# Guide 2 scores for plotting
			indExpScore2 = indGuide2Feedback['Exp Score']
			indGuideScore2 = indGuide2Feedback['Guide Score']
			indRouteScore2 = indGuide2Feedback['Route Score']
			# Checking guide name spelling

			# Joint Experience score Histograms
			f,ax = plt.subplots(figsize = (8,5))
			ax.hist(indExpScore1, bins = 5, color = purpleNU, label = guideName1)#histogram with Northwestern purple Go 'Cats
			ax.hist(indExpScore2, bins = 5, color = greyNU, label = guideName2)#histogram with Northwestern purple Go 'Cats
			ax.set_xlim((0,6))
			ax.set_ylim((0,6))
			ax.set_xlabel('Visitors\' experience scores')
			ax.set_title(guideName1 + ' & '  + guideName2)
			ax.legend()

			# joint Route score histograms
			f,ax = plt.subplots(figsize = (8,5))
			ax.hist(indRouteScore1, bins = 5, color = purpleNU, label = guideName1)
			ax.hist(indRouteScore2, bins = 5, color = greyNU, label = guideName2)
			ax.set_xlim((0,6))
			ax.set_ylim((0,6))
			ax.set_xlabel('Visitors\' Route Scores')
			ax.set_title(guideName1 + ' & '  + guideName2)
			ax.legend()

			# joint guide score histograms
			f,ax = plt.subplots(figsize = (8,5))
			ax.hist(indGuideScore1, bins = 5, color = purpleNU, label = guideName1)
			ax.hist(indGuideScore2, bins = 5, color = greyNU, label = guideName2)
			ax.set_xlim((0,6))
			ax.set_ylim((0,6))
			ax.set_xlabel('Guide Score')
			ax.set_title(guideName1 + ' & '  + guideName2)
			ax.legend()

			# ######### Scatter plots to see score correlations between scoring techniques ###########

			# joint Guide Score - Exp Score
			f,ax = plt.subplots(figsize = (8,5))
			ax.scatter(indGuideScore1, indExpScore1, color = purpleNU, label = guideName1)
			ax.scatter(indGuideScore2, indExpScore2, color = greyNU, marker = '^', label = guideName2)
			ax.set_xlim((0,6))
			ax.set_ylim((0,6))
			ax.set_xlabel('Guide Score')
			ax.set_ylabel('Experience Score')
			ax.set_title(guideName1 + ' & '  + guideName2)
			ax.legend()

			# joint route Score - Exp Score
			f,ax = plt.subplots(figsize = (8,5))
			ax.scatter(indRouteScore1, indExpScore1, color = purpleNU, label = guideName1)
			ax.scatter(indRouteScore2, indExpScore2, color = greyNU, marker = '^', label = guideName2)
			ax.set_xlim(0,6)
			ax.set_ylim((0,6))
			ax.set_xlabel('Route Score')
			ax.set_ylabel('Experience Score')
			ax.set_title(guideName1 + ' & '  + guideName2)
			ax.legend()

			plt.show()


				# Setting up input buttons on entry widget
		quitButton = tk.Button(self.master, text='Quit', command= self.master.quit).grid(row=3, column=0, sticky=tk.W, pady=4)#Quit button
		backButton = tk.Button(self.master, text = 'Back', command = self.master.quit).grid(row=3, column =1, sticky=tk.W, padx = 5,pady=5)#Back button
		plotsButton = tk.Button(self.master, text='View Feedback', command = jointPlots).grid(row=3, column=1, sticky=tk.W, padx = 5,pady=5)#Plots button



		##################################### OLD Stuff###################################
		# searchType = input('Would you like to search a joint pair of guides?[y/n]: ')
		# if 'y' in searchType:

		# 	name1 = input('Guide 1 Name: ')
		# 	name2 = input('Guide 2 Name: ')
		# 	Timestamp = feedback['Timestamp']

		# 	guidetime1 = Timestamp.loc[names == name1]
		# 	guidetime2 = Timestamp.loc[names == name2]

		# 	guideName1 = feedback.loc[names == name1]
		# 	guideName2 = feedback.loc[names == name2]

		# 	# If timestamps are the same, they should be considered a joint pairing
		# 	pairName = guideName1 + guideName2
		# 	print(pairName)


		# 	# Insert makePlots() here
		# 	self.makePlots(name1, name2)

		# 	return guidetime1, guidetime2

			# Kill function if the user inputs 'no'
		# else: 
		# 	print('Goodbye...')
		# 	pass

		##################################### OLD - from jointing.py #########################



	def searchType(self):
		"""
		Function to determine search type from User (All or individual guide search)

		"""
		self.master1 = tk.Tk()

		tk.Label(self.master1, text = 'Would you like to view feedback for all guides or an individual guide?').grid(row=0, padx = 5, pady=5)#Command question (displayed above buttons)
		tk.Button(self.master1, text = 'All', command = self.makePlots).grid(row=1, column=0, sticky=tk.W , padx = 5, pady=5)#All guide scatter
		tk.Button(self.master1, text = 'Individual', command = self.guideSearch).grid(row=2, column=0, sticky=tk.W, padx = 5, pady=5)#Individual Search
		tk.Button(self.master1, text = 'Joint Pair', command = self.pairSearch).grid(row=3, column=0, sticky=tk.W, padx = 5, pady=5) # Joint pair search
		tk.Button(self.master1, text = 'Quit', command = self.master1.quit).grid(row=4, column=0, sticky=tk.W, padx = 5, pady=5)#Quit Button


		# Runs searchType widget
		self.master1.mainloop()

	def RunAll(self):
		
		self.searchType()
		self.guideSearch()
		# self.show_entry_fields()


test1 = Search()
test1.RunAll()

# Search class is working well, can make more aesthetically pleasing with themed Tkinter 
# popup is almost ready to integrate - maybe add a 'Back' button to guideSearch

######################################## WORKING SECTION - GUIDE SEARCH ################################################################
										

											###################################
										###########################################
							# ######### BELOW FUNCTIONS ARE COPIED INTO CLASS ABOVE ############
										###########################################
											###################################

# def guideSearch():
# 	master = tk.Tk()

# 	tk.Label(master, text="First Name").grid(row=0)
# 	tk.Label(master, text="Last Name").grid(row=1)

# 	e1 = tk.Entry(master)
# 	e2 = tk.Entry(master)
# 	e3 = tk.Entry(master)

# 	firstName = e1.grid(row=0, column=1)
# 	lastName = e2.grid(row=1, column=1)


# 	# Stuff to add buttons
# 	def show_entry_fields():
# 		"""Function to call for our buttons when a guide's name is searched"""

# 		print("First Name: %s\nLast Name: %s" % (e1.get(), e2.get()))
# 		import matplotlib.pyplot as plt
# 		x = np.random.random(100)
# 		y = np.random.random(100)
# 		GuideName = e1.get() + ' ' + e2.get()
# 		f,ax = plt.subplots()
# 		ax.scatter(x,y)
# 		ax.set_title(GuideName)
# 		plt.show()


# 	# Setting up input buttons on entry widget
# 	tk.Button(master, text='Quit', command=master.quit).grid(row=3, column=0, sticky=tk.W, pady=4)
# 	tk.Button(master, text='View Feedback', command=show_entry_fields).grid(row=3, column=1, sticky=tk.W, padx = 5,pady=5)



# 	# master.mainloop()

# ############################################## TESTING ALL/IND INPUT WIDGET INTO SECOND ###################################################################

# def randomScat():
# 	"""Random scatter plot with title set to search type"""
# 	import matplotlib.pyplot as plt
# 	x = np.random.random(100)
# 	y = np.random.random(100)
# 	f,ax = plt.subplots()
# 	ax.scatter(x,y)
# 	ax.set_title('All Guides')
# 	plt.show()



# def searchType():
# 	"""
# 	Function to determine search type from User (All or individual guide search)

# 	"""
# 	master1 = tk.Tk()

# 	tk.Label(master1, text = 'Individual Guide or All guide feedback?').grid(row=0)
# 	tk.Button(master1, text = 'All', command = randomScat).grid(row=1, column=0, sticky=tk.W)#All guide scatter
# 	tk.Button(master1, text = 'Individual', command = guideSearch).grid(row=1, column=1, sticky=tk.W, padx = 4,pady=4)#Individual Search
# 	tk.Button(master1, text = 'Quit', command = master1.quit).grid(row=1, column=2, sticky=tk.W, padx = 4,pady=4)#Quit Button

# 	# master1.mainloop()

# # test = searchType()








