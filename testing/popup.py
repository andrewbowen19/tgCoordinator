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


# ################################################### Writing this as a class ####################################

class Search(object):

	def __init__(self):
		self.name = None

	# This works
	def guideSearch(self):
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
			import matplotlib.pyplot as plt
			x = np.random.random(100)
			y = np.random.random(100)
			GuideName = self.e1.get() + ' ' + self.e2.get()
			f,ax = plt.subplots()
			ax.scatter(x,y)
			ax.set_title(GuideName)
			plt.show()


		# Setting up input buttons on entry widget
		tk.Button(self.master, text='Quit', command= self.master.quit).grid(row=3, column=0, sticky=tk.W, pady=4)
		tk.Button(self.master, text='View Feedback', command = show_entry_fields).grid(row=3, column=1, sticky=tk.W, padx = 5,pady=5)

		# Runs individual search widget
		# self.master.mainloop()


	def randomScat(self):
		"""Random scatter plot with title set to search type 
		PLACEHOLDER FUNCTION TO BE REPLACED WITH FUCNTIONS FOR IND GUIDE PLOTS OR ALL GUIDE PLOTS
		"""
		import matplotlib.pyplot as plt
		x = np.random.random(100)
		y = np.random.random(100)
		f,ax = plt.subplots()
		ax.scatter(x,y)
		ax.set_title('All Guides')
		plt.show()

	def searchType(self):
		"""
		Function to determine search type from User (All or individual guide search)

		"""
		self.master1 = tk.Tk()

		tk.Label(self.master1, text = 'Individual Guide or All guide feedback?').grid(row=0)
		tk.Button(self.master1, text = 'All', command = self.randomScat).grid(row=1, column=0, sticky=tk.W)#All guide scatter
		tk.Button(self.master1, text = 'Individual', command = self.guideSearch).grid(row=1, column=1, sticky=tk.W, padx = 4,pady=4)#Individual Search
		tk.Button(self.master1, text = 'Quit', command = self.master1.quit).grid(row=1, column=2, sticky=tk.W, padx = 4,pady=4)#Quit Button

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
							# ######### BELOW FUNCTIONS ARE COPIED INTO CODE ABOVE ############
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








