# Feedback system for the tour guide program:
# Northwestern Univeristy Office of Undergraduate Admissions
# Segal Visitor's Center
# 1841 Hinman Ave, Evanston, IL, 60201
# Author: Andrew Bowen
# License: MIT License

'''Script to make plots for all readers we had last year, can do for this year too (with new data sheet)'''

import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import matplotlib as mpl
from matplotlib import gridspec
import matplotlib.cm as cm
import os


path_to_data = '/Users/andrewbowen/tgCoordinator/hiring/data/'
data = pd.read_csv('./reader-scores.csv')


# renaming dtaframe columns 
new_names = ['Timestamp', 'Reader', 'Applicant ID #', 'Applicant ID # Confirm',
	 'Reader #', 'Appropriate', 'Campus Awareness', 'Originality', 'Thoroughness', 
	 'Campus Involvement', 'Video (Y/N)', 'Comments', 'Reasons for Concern', 'Schools', 'Majors']
data.columns = new_names


def readerPlots(Reader):
	'''Function to make different plots for each reader'''
	reader = data.loc[np.where(data['Reader'] == Reader)]
	readerName = reader['Reader'].values[0] # string of reader name

	xbins = np.arange(0,6,1)

	dirName = Reader.replace(' ', '-') # remvoing spaces for directory names


	# setting up directory for their plots and individual csv score file
	os.mkdir(f'./scorers/{dirName}')
	os.mkdir(f'./scorers/{dirName}/plots/')
	os.mkdir(f'./scorers/{dirName}/data/')


	# Histograms - Appropriate scores given
	f,ax = plt.subplots()
	ax.hist(reader['Appropriate'], range = (0,5), bins = 5)
	ax.set_title(Reader)
	ax.set_xlabel('Appropriate')
	f.savefig(f'./scorers/{dirName}/plots/{dirName}-Appropriate-hist.pdf')


	# Histograms: Originality scores
	f,ax = plt.subplots()
	ax.hist(reader['Originality'], range = (0,5), bins = 5)
	ax.set_title(Reader)
	ax.set_xlabel('Originality')
	f.savefig(f'./scorers/{dirName}/plots/{dirName}-Originality-hist.pdf')


	# Histograms - Campus Awareness
	f,ax = plt.subplots()
	ax.hist(reader['Campus Awareness'], range = (0,5), bins = 5)
	ax.set_title(Reader)
	ax.set_xlabel('Campus Awareness')
	f.savefig(f'./scorers/{dirName}/plots/{dirName}-CampusAwareness-hist.pdf')


# ############# Mixture plots - correlations between types of scores ################
# Time for me to have some fun

	# Fun mixing plots
	# Limits for 2d histograms
	xmin, xmax, Nx = 0, 5, 5
	ymin, ymax, Ny = 0, 5, 5

	# Appropriate-Originality 2d Histogram (shows where people are scoring each of these measures)
	f,ax = plt.subplots()
	h2d, x2D, y2D, im = ax.hist2d(reader['Appropriate'], reader['Originality'], bins = [Nx, Ny],
		 range = [[xmin, xmax],[ymin, ymax]], normed = True, cmap = cm.Blues)
	ax.set_xlabel('Appropriate')
	ax.set_ylabel('Originality')
	ax.set_title(Reader)
	cbar = f.colorbar(im, ax = ax)
	cbar.ax.set_yticklabels(np.arange(0,100,20)) # percentages up too 100%
	cbar.ax.set_ylabel('% Scores', rotation = 270, labelpad = 8)
	f.savefig(f'./scorers/{dirName}/plots/{dirName}-AppOrg-hist2d.pdf')

	# 2D hist of Appropriate versus Campus Awareness scores
	f,ax = plt.subplots()
	h2d, x2D, y2D, im = ax.hist2d(reader['Appropriate'], reader['Campus Awareness'], bins = [Nx, Ny],
		 range = [[xmin, xmax],[ymin, ymax]], normed = True, cmap = cm.Blues)
	ax.set_xlabel('Appropriate')
	ax.set_ylabel('Campus Awareness')
	ax.set_title(Reader)
	cbar = f.colorbar(im, ax = ax)
	cbar.ax.set_yticklabels(np.arange(0,100,20)) # percentages up too 100%
	cbar.ax.set_ylabel('% Scores', rotation = 270, labelpad = 8)
	f.savefig(f'./scorers/{dirName}/plots/{dirName}-AppCA-hist2d.pdf')

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
	f.savefig(f'./scorers/{dirName}/plots/{dirName}-OrgCA-hist2d.pdf')


	# Saving all data for that reader in their own csv file
	reader.to_csv(f'./scorers/{dirName}/data/{dirName}-scoring-data.csv')


readerNames = np.unique(data['Reader'])

for name in readerNames:
	print('Making plots and csv files for: ', name)
	readerPlots(name)
	print('Plots and csv made! Onto the next... \n')

	




