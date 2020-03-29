# Writing class for application to make guide plots -- shedding tkinter

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd



class GuidePlots(object):

	def __init__(self, guideName):
		self.guideName = None

	def scatterPlot(self, guideName, x_scores, y_scores, xlabel, ylabel, best_fit = False, saveFig = True):
		'''
		Method to create scatter plots to see correlations between two scores for a guide
		Not very useful if our scores are discrete values - 2d histogram method would be better
		'''
		f, ax = plt.subplots()
		ax.scatter(x_scores, y_scores)
		ax.set_xlim(0,5)
		ax.set_ylim(0,5)
		ax.set_title(guideName)
		ax.set_xlabel(xlabel)
		ax.set_ylabel(ylabel)

		if saveFig:
			f.savefig(f'{guideName}-{xlabel}-{ylabel}-scatter.pdf')

	def hist1D(self, guideName, scores,xlabel, best_fit = True, saveFig = True):
		'''
		Function to create 1d histogram for whatever guide score parameter we want
		if best_fit = True, guide 
		'''
		f,ax = plt.subplots()
		ax.hist(scores, bins = 5) # using 5 bins because current score scale is 0-5 (subject to change)
		ax.set_xlabel(xlabel)

		if saveFig:
			f.savefig(f'{guideName}-{xlabel}-hist.pdf')




















