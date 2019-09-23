# Feedback system for the tour guide program:
# Northwestern Univeristy Office of Undergraduate Admissions
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
# Ussing themed tkinter widgets (ttk) to create more modern-looking GUIs
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

		# Setting up input buttons on entry widget
		quitButton = tk.Button(self.master, text='Quit', command= self.master.quit).grid(row=3, column=0, sticky=tk.W, pady=4)#Quit button
		backButton = tk.Button(self.master, text = 'Back', command = self.master.quit).grid(row=3, column =1, sticky=tk.W, padx = 5,pady=5)#Back button
		plotsButton = tk.Button(self.master, text='View Feedback', command = makeGuidePlots).grid(row=3, column=1, sticky=tk.W, padx = 5,pady=5)#Plots button

		# Works for now, will need to add name spelling checks (or could clean that up before adding names to our db)


	def searchType(self):
		"""
		Function to determine search type from User (All or individual guide search)

		"""
		self.master1 = tk.Tk()

		tk.Label(self.master1, text = 'Would you like to view feedback for all guides or an individual guide?').grid(row=0, padx = 5, pady=5)#Command question (displayed above buttons)
		tk.Button(self.master1, text = 'All', command = self.makePlots).grid(row=1, column=0, sticky=tk.W , padx = 5, pady=5)#All guide scatter
		tk.Button(self.master1, text = 'Individual', command = self.guideSearch).grid(row=2, column=0, sticky=tk.W, padx = 5, pady=5)#Individual Search
		tk.Button(self.master1, text = 'Quit', command = self.master1.quit).grid(row=3, column=0, sticky=tk.W, padx = 5,pady=5)#Quit Button

		# Runs searchType widget
		self.master1.mainloop()

	def RunAll(self):
		self.searchType()
		self.guideSearch()

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







