# Feedback system for the tour guide program:
# Northwestern Univeristy Office of Undergraduate Admissions
# Segal Visitor's Center
# 1841 Hinman Ave, Evanston, IL, 60201
# Author: Andrew Bowen
# License: MIT License

'''Script to make plots for all readers we had last year, can do for this year too (with new data sheet)
	NON-interactive, only loops through readers and makes plots/creates stat dataframes'''

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


	# setting up directory for their plots and individual csv score file if they don't already exist (if they do, files are saved to existing scorer file)
	if not os.path.isdir(f'./scorers/{dirName}'):
		os.mkdir(f'./scorers/{dirName}')

	if not os.path.isdir(f'./scorers/{dirName}/plots/'):

		os.mkdir(f'./scorers/{dirName}/plots/')

	if not os.path.isdir(f'./scorers/{dirName}/data/'):
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


# #######################################################################################################

def readerStats(readerName):
	'''Function that returns stats for our readers (mean scores, # of apps readm etc)'''
	datReader = data.loc[np.where(data['Reader'] == readerName)]
	readerDir = readerName.replace(' ', '-')
	numRead = len(datReader) # # of apps read

	# Means and std devs for each scoring section
	meanApp = np.mean(datReader['Appropriate'])
	meanOrg = np.mean(datReader['Originality'])
	meanCA = np.mean(datReader['Campus Awareness'])

	stdApp = np.std(datReader['Appropriate'])
	stdOrg = np.std(datReader['Originality'])
	stdCA = np.std(datReader['Campus Awareness'])

	# Setting up dataframe - can store in separate csv file for easier reading
	columns = ['Name' ,'Napps', 'App mean', 'App std','Org mean', 'Org std','CA mean', 'CA std']
	dat = {'Name':readerName,'Napps' : numRead,'App mean': meanApp,  'App std': stdApp, 
		'Org mean': meanOrg,'Org std' :stdOrg,'CA mean': meanCA, 'CA std': stdCA}
	stats = pd.DataFrame(dat, index = [0])
	stats.to_csv(f'./scorers/{readerDir}/data/{readerDir}-stats.csv') # sending individual data to csv file in each scorer's directory

	return stats


readerNames = np.unique(data['Reader'])
columns = ['Name','Napps', 'App mean', 'App std','Org mean', 'Org std','CA mean', 'CA std']
allList = []

# Looping through each reader and creating plots/stat sheets for them
for name in readerNames:
	print('Making plots and csv files for: ', name)
	readerPlots(name)
	indStats = readerStats(name)
	allList.append(indStats) # Appending individual dataframes to create all dataframes


	print('Plots and csv made! Onto the next... \n')

# Creating csv file with stats breakdown for each reader for all readers
all_stats = pd.concat(allList, ignore_index = True)
print(all_stats)
all_stats.to_csv('./data/reader-stats.csv')

# #######################################################################################################
# Printing out nicest and meanest readers and their respective scores

print('')
print('###################################')

print('Nicest for Appropriate: ', all_stats['Name'][all_stats['App mean'].idxmax()], '(',np.max(all_stats['App mean']), ')') #.loc[np.argmax(all_stats['App mean'])])
print('Nicest for Originality: ', all_stats['Name'][all_stats['Org mean'].idxmax()], '(',np.max(all_stats['Org mean']), ')')
print('Nicest for Campus Awareness: ',  all_stats['Name'][all_stats['CA mean'].idxmax()], '(',np.max(all_stats['CA mean']), ')')
print('Most apps read: ', all_stats['Name'][all_stats['Napps'].idxmax()], '(',np.max(all_stats['Napps']), ')')

print('###################################')

print('Meanest for Appropriate: ', all_stats['Name'][all_stats['App mean'].idxmin()], '(',np.min(all_stats['App mean']), ')')
print('Meanest for Originality: ', all_stats['Name'][all_stats['Org mean'].idxmin()], '(',np.min(all_stats['Org mean']), ')')
print('Meanest for Campus Awareness: ',  all_stats['Name'][all_stats['CA mean'].idxmin()], '(',np.min(all_stats['CA mean']), ')')
print('Least apps read: ', all_stats['Name'][all_stats['Napps'].idxmin()], '(',np.min(all_stats['Napps']), ')')

# #######################################################################

# Making some plots from all reader data
xmin, xmax, Nx = 0,5,10
ymin, ymax, Ny = 0,5,10

# 2D hist of mean scores for 'Appropriate' versus 'Originality'
f,ax = plt.subplots()
h2d, x2D, y2D, im = ax.hist2d(all_stats['App mean'], all_stats['Org mean'], bins = [Nx, Ny],
	 range = [[xmin, xmax],[ymin, ymax]], cmap = cm.Blues)
ax.set_xlabel('Appropriate mean')
ax.set_ylabel('Originality mean')
ax.set_title('All Readers')
cbar = f.colorbar(im, ax = ax)
cbar.ax.set_ylabel('N Scores', rotation = 270, labelpad = 8)
f.savefig(f'./plots/All-AppOrg-hist2d.pdf')

# 2D hist for mean Appropriate vs mean Campus Awareness scores
f,ax = plt.subplots()
h2d, x2D, y2D, im = ax.hist2d(all_stats['App mean'], all_stats['CA mean'], bins = [Nx, Ny],
	 range = [[xmin, xmax],[ymin, ymax]], cmap = cm.Blues)
ax.set_xlabel('Appropriate Scores mean')
ax.set_ylabel('Campus Awareness Scores mean')
ax.set_title('All Readers')
cbar = f.colorbar(im, ax = ax)
cbar.ax.set_ylabel('N Scores', rotation = 270, labelpad = 8)
f.savefig(f'./plots/All-AppCA-hist2d.pdf')

# 2D hist for mean Originality vs mean Campus Awareness scores
f,ax = plt.subplots()
h2d, x2D, y2D, im = ax.hist2d(all_stats['Org mean'], all_stats['CA mean'], bins = [Nx, Ny],
	 range = [[xmin, xmax],[ymin, ymax]], cmap = cm.Blues)
ax.set_xlabel('Originality Scores mean')
ax.set_ylabel('Campus Awareness Scores mean')
ax.set_title('All Readers')
cbar = f.colorbar(im, ax = ax)
cbar.ax.set_ylabel('N Scores', rotation = 270, labelpad = 8)
f.savefig(f'./plots/All-OrgCA-hist2d.pdf')

# 1D hists:
f,ax = plt.subplots()
ax.hist(all_stats['App mean'], label = 'Appropriate')
ax.hist(all_stats['Org mean'], alpha = 0.5, label = 'Originality')
ax.hist(all_stats['CA mean'], alpha = 0.5, label = 'Campus Awareness')
ax.set_xlabel('Scores')
ax.legend()
f.savefig('./plots/hist1D-categories.pdf')

# Scater plots - Appropriate-Originality
f,ax = plt.subplots()
ax.scatter(all_stats['App mean'], all_stats['Org mean'])
ax.set_xlabel('Appropriate Scores')
ax.set_ylabel('Originality Scores')
ax.set_title('All readers')
f.savefig('./plots/AppOrg-scatter.pdf')

# scatter Appropriate - Campus Awareness
f,ax = plt.subplots()
ax.scatter(all_stats['App mean'], all_stats['CA mean'])
ax.set_xlabel('Appropriate Scores')
ax.set_ylabel('Campus Awareness Scores')
ax.set_title('All readers')
f.savefig('./plots/AppCA-scatter.pdf')

# Scatter Originality - Campus Awareness
f,ax = plt.subplots()
ax.scatter(all_stats['Org mean'], all_stats['CA mean'])
ax.set_xlabel('Originality Scores')
ax.set_ylabel('Campus Awareness Scores')
ax.set_title('All readers')
f.savefig('./plots/OrgCA-scatter.pdf')

#Could incluse ind scatter plots to show all scores for an ind reader







	




