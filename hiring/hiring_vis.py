# Feedback system for the tour guide program:
# Northwestern Univeristy Office of Undergraduate Admissions
# Segal Visitor's Center
# 1841 Hinman Ave, Evanston, IL, 60201
# Author: Andrew Bowen
# License: MIT License

'''Script to create visualizations from our TG hiring forms (get csv files)'''

import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import matplotlib as mpl
from matplotlib import gridspec
import matplotlib.cm as cm
import os

data = pd.read_csv('./data/reader-scores.csv')


# renaming dtaframe columns 
new_names = ['Tiemstamp', 'Reader', 'Applicant ID #', 'Applicant ID # Confirm',
	 'Reader #', 'Appropriate', 'Campus Awareness', 'Originality', 'Thoroughness', 
	 'Campus Involvement', 'Video (Y/N)', 'Comments', 'Reasons for Concern', 'Schools', 'Majors']
data.columns = new_names

yes_answers = ['y', 'Y', 'yes', 'Yes', 'YES', 'YeS', 'yEs', 'yeS']
no_answers = ['n', 'N', 'NO', 'no', 'No','nO']

def searchAgain():
	newSearch = input('Would you like to search for more scores? [y/n]: ')

	if newSearch in yes_answers:
		return True
	else:
		return False


# Could also write function to check how readers grade
def appPlots(appID, plotType):
	'''function to make different plots for each guide, 
		will need to think of how we deal with spread of only 2 readers'''
	applicant = data.loc[np.where(data['Applicant ID #'] == appID)]
	xbins = np.arange(0,5,1)


	keepSearching = True
	while keepSearching == True:
	
		if plotType == 'App':
			# Histograms - Appropriate
			f,ax = plt.subplots()
			ax.hist(applicant['Appropriate'], range = (0,5), bins = 5)
			ax.set_title(appID)
			ax.set_xlabel('Appropriate')
			plt.show()

			keepSearching = searchAgain() # Check to see if user wants to keep searching

		elif plotType == 'Org':
			# Histograms - Originality
			f,ax = plt.subplots()
			ax.hist(applicant['Orginality'], range = (0,5), bins = 5)
			ax.set_title(appID)
			ax.set_xlabel('Originality')
			plt.show()

			keepSearching = searchAgain() # Check to see if user wants to keep searching

		elif plotType == 'CA':
			# Histograms - Campus Awareness
			f,ax = plt.subplots()
			ax.hist(applicant['Campus Awareness'], range = (0,5), bins = 5)
			ax.set_title(appID)
			ax.set_xlabel('Campus Awareness')
			plt.show()

			keepSearching = searchAgain() # Check to see if user wants to keep searching

# ############# Mixture plots - correlations between types of scores ################
# Time for me to have some fun

		elif plotType == 'Mix':
			# Fun mixing plots

			# Limits for 2d histograms
			xmin, xmax, Nx = 0, 5, 5
			ymin, ymax, Ny = 0, 5, 5

			# Appropriate -Originality 2d Histogram (shows where people are scoring each of these measures)
			f,ax = plt.subplots()
			h2d, x2D, y2D, im = ax.hist2d(applicant['Appropriate'], applicant['Originality'], bins = [Nx, Ny],
				 range = [[xmin, xmax],[ymin, ymax]], cmap = cm.Blues)
			ax.set_xlabel('Appropriate')
			ax.set_ylabel('Originality')
			ax.set_title(appID)
			cbar = f.colorbar(im, ax = ax)
			cbar.ax.set_yticklabels(np.arange(0,100,20)) # percentages up too 100%
			cbar.ax.set_ylabel('% Scores', rotation = 270, labelpad = 8)
			

			# 2D hist of cmapus awareness vs appropriate
			f,ax = plt.subplots()
			h2d, x2D, y2D, im = ax.hist2d(applicant['Appropriate'], applicant['Campus Awareness'], bins = [Nx, Ny],
				 range = [[xmin, xmax],[ymin, ymax]], cmap = cm.Blues)
			ax.set_xlabel('Appropriate')
			ax.set_ylabel('Campus Awareness')
			ax.set_title(appID)
			cbar = f.colorbar(im, ax = ax)
			cbar.ax.set_yticklabels(np.arange(0,100,20)) # percentages up too 100%
			cbar.ax.set_ylabel('% Scores', rotation = 270, labelpad = 8)

			f,ax = plt.subplots()
			h2d, x2D, y2D, im = ax.hist2d(applicant['Originality'], applicant['Campus Awareness'], bins = [Nx, Ny],
				 range = [[xmin, xmax],[ymin, ymax]], cmap = cm.Blues)
			ax.set_xlabel('Originality')
			ax.set_ylabel('Campus Awareness')
			ax.set_title(appID)
			cbar = f.colorbar(im, ax = ax)
			cbar.ax.set_yticklabels(np.arange(0,100,20)) # percentages up too 100%
			cbar.ax.set_ylabel('% Scores', rotation = 270, labelpad = 8)

			plt.show()


			keepSearching = searchAgain() # Check to see if user wants to keep searching



def readerPlots(Reader, plotType):
	'''Function to make different plots for each reader'''
	reader = data.loc[np.where(data['Reader'] == Reader)]
	readerName = reader['Reader'].values[0] # string of reader name

	xbins = np.arange(0,6,1)

	keepSearching = True
	while keepSearching == True:

		# Histograms - Appropriate
		if plotType == 'App' or plotType.lower() == 'app':
			
			f,ax = plt.subplots()
			ax.hist(reader['Appropriate'], range = (0,5), bins = 5)
			ax.set_title(Reader)
			ax.set_xlabel('Appropriate')
			plt.show()

			keepSearching = searchAgain() # Check to see if user wants to keep searching
		# Histograms - Originality
		elif plotType == 'Org' or plotType.lower() == 'org':

			f,ax = plt.subplots()
			ax.hist(reader['Orginality'], range = (0,5), bins = 5)
			ax.set_title(Reader)
			ax.set_xlabel('Originality')
			plt.show()

			keepSearching = searchAgain() # Check to see if user wants to keep searching

		# Histograms - Campus Awareness
		elif plotType == 'CA' or plotType.lower() == 'ca':

			f,ax = plt.subplots()
			ax.hist(reader['Campus Awareness'], range = (0,5), bins = 5)
			ax.set_title(Reader)
			ax.set_xlabel('Campus Awareness')
			plt.show()

			keepSearching = searchAgain() # Check to see if user wants to keep searching

# ############# Mixture plots - correlations between types of scores ################
# Time for me to have some fun

		elif plotType == 'Mix' or plotType.lower() == 'mix':
			# Fun mixing plots
			# Limits for 2d histograms
			xmin, xmax, Nx = 0, 5, 5
			ymin, ymax, Ny = 0, 5, 5

			# Appropriate -Originality 2d Histogram (shows where people are scoring each of these measures)
			f,ax = plt.subplots()
			h2d, x2D, y2D, im = ax.hist2d(reader['Appropriate'], reader['Originality'], bins = [Nx, Ny],
				 range = [[xmin, xmax],[ymin, ymax]], normed = True, cmap = cm.Blues)
			ax.set_xlabel('Appropriate')
			ax.set_ylabel('Originality')
			ax.set_title(Reader)
			cbar = f.colorbar(im, ax = ax)
			cbar.ax.set_yticklabels(np.arange(0,100,20)) # percentages up too 100%
			cbar.ax.set_ylabel('% Scores', rotation = 270, labelpad = 8)

			# 2D hist of cmapus awareness vs appropriate
			f,ax = plt.subplots()
			h2d, x2D, y2D, im = ax.hist2d(reader['Appropriate'], reader['Campus Awareness'], bins = [Nx, Ny],
				 range = [[xmin, xmax],[ymin, ymax]], normed = True, cmap = cm.Blues)
			ax.set_xlabel('Appropriate')
			ax.set_ylabel('Campus Awareness')
			ax.set_title(Reader)
			cbar = f.colorbar(im, ax = ax)
			cbar.ax.set_yticklabels(np.arange(0,100,20)) # percentages up too 100%
			cbar.ax.set_ylabel('% Scores', rotation = 270, labelpad = 8)

			# 2D hist of Campus awareness vs originality
			f,ax = plt.subplots()
			h2d, x2D, y2D, im = ax.hist2d(reader['Originality'], reader['Campus Awareness'], bins = [Nx, Ny],
				 range = [[xmin, xmax],[ymin, ymax]], normed = True, cmap = cm.Blues)
			ax.set_xlabel('Originality')
			ax.set_ylabel('Campus Awareness')
			ax.set_title(Reader)
			cbar = f.colorbar(im, ax = ax)
			cbar.ax.set_yticklabels(np.arange(0,100,20)) # percentages up too 100%
			cbar.ax.set_ylabel('% Scores', rotation = 270, labelpad = 8)



			plt.show()

			keepSearching = searchAgain()







# #################################################################################################################
def scoreSearch():
	search = input('Would you like to search an applicant or reader [a/r]: ')

	if search == 'a' or search == 'A':
		# Applicant search
		appNum = input('Enter applicant ID #: ')
		plot = input('What kind of plot would you like to visualize (please select)?: ')
		print('Appropriate Scores (App) \n Originality Scores (Org) \n Campus Awareness Scores (CA) \n Mix')

		appPlots(appNum, plot)

	if search == 'r' or search == 'R':
		# Reader search
		reader = input('Enter Reader Name: ')

		print('Appropriate Scores (App) \nOriginality Scores (Org) \nCampus Awareness Scores (CA) \nMix')
		print('')
		plot = input('What kind of plot would you like to visualize (please select from above)?: ')


		readerPlots(reader, plot)



scoreSearch()













