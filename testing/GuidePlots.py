'''
Writing class for application to make guide plots -- shedding tkinter
'''

# Tour Guide Program : Feedback system
# Northwestern Univeristy Office of Undergraduate Admissions
# Segal Visitors' Center
# 1841 Hinman Ave, Evanston, IL, 60201
# Author: Andrew Bowen
# License: MIT License

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import matplotlib.cm as cm


class GuidePlots(object):
	'''
	Class to generate plots and data visualizations for django web-based app
	Need to 
	'''

	def __init__(self, guideName):
		self.guideName = None

	def scatterPlot(self, guideName, x_scores, y_scores, xlabel, ylabel, best_fit = False, saveFig = True):
		'''
		Method to create scatter plots to see correlations between two scores for a guide
		Not very useful if our scores are discrete values - 2d histogram method would be better
		Both x and y scores need to be array-like to plot correctly
		'''
		self.guideName = guideName

		f, ax = plt.subplots()
		ax.scatter(x_scores, y_scores)
		ax.set_xlim(0,5)
		ax.set_ylim(0,5)
		ax.set_title(guideName)
		ax.set_xlabel(xlabel)
		ax.set_ylabel(ylabel)

		if saveFig:
			f.savefig(f'{guideName}-{xlabel}-{ylabel}-scatter.pdf')

	def hist1D(self, guideName, scores,xlabel, best_fit = True, saveFig = False):
		'''
		Method to create 1d histogram for whatever guide score parameter we want
		if best_fit = True, will fit gaussian to histogram 
		Both x and y scores need to be array-like to plot correctly
		'''
		self.guideName = guideName

		f,ax = plt.subplots()
		ax.hist(scores, bins = 5) # using 5 bins because current score scale is 0-5 (subject to change)
		ax.set_xlabel(xlabel)

		if saveFig:
			f.savefig(f'{self.guideName}-{xlabel}-hist.pdf')


	def hist2D(self, guideName, xscores, yscores, xlabel, ylabel, Nx, Ny, xmin, xmax, ymin, ymax, saveFig = False, path_to_fig = None):
		'''
		Method to create 2d histogram to see cross-correlations between scores
		if saveFig = True, will save figure to the path provided in path_to_fig (default False, None)
		Both x and y scores need to be array-like to plot correctly
		'''


		self.guideName = guideName

		# creating figure
		f,ax = plt.subplots(figsize = (8,5))
		h2d, x2D, y2D, im  = h2d, x2D, y2D, im  = ax.hist2d(xscores, yscores, bins=[Nx, Ny], \
			range=[[xmin, xmax], [ymin, ymax]], cmap = cm.Blues)
		ax.set_xlabel('Guide Score')
		ax.set_ylabel('Experience Score')
		ax.set_title(self.guideName)
		cbar = f.colorbar(im)
		cbar.ax.set_ylabel(r'# Scores', rotation = 270, labelpad = 8)





















