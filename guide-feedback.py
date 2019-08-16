# Feedback system for the tour guide program:
# Northwestern Univeristy Office of Undergraduate Admissions
# 1841 Hinman Ave, Evanston, IL, 60201
# Author: Andrew Bowen



"""
Script for us to read in TG feedback and send it to the correct TG feedback file 
(to be posted on google drive).
Want guides to have feedback visible only to them and coordinators (from coordinator account)

"""

# Importing needed modules
import pandas as pd
import matplotlib.pyplot as plt

# Reading in visitor feedback files (responses for every guide/tour)
path = '/Users/andrewbowen/tgCoordinator/'
feedback = pd.read_csv(path + 'Feedback_Form_Beta.csv', sep = ',',header = 0)

# Renaming the columns for easier readability
feedback.columns = ['Timestamp','Visitor Name', 'Visitor Email', 'Visitor Type', 'Visit Date', 'Guide Name',\
			'Exp Score', 'Route Score', 'Guide Score', 'Comments']

# Scores for plotting later
expScore = feedback['Exp Score']
guideScore = feedback['Guide Score']
routeScore = feedback['Route Score']

names = feedback['Guide Name']

# Want to be able to type in guide's name, pull out the correct data frame, and write that to a file
guideName = input('Guide Name: ')
indGuideFeedback = feedback.loc[names == guideName]
guideName = guideName.replace(' ', '_')#replacing spaces for file name cleanliness

# Setting up individual files for each guide
newpath = '/Users/andrewbowen/tgCoordinator/indFiles/'
guideFile = indGuideFeedback.to_csv(newpath + f'{guideName}_feedback.csv')




# ##################################################### Visualization ######################################################

# Can create histograms of scores if we want

# Experience score
# f,ax = plt.subplots(figsize = (8,5))
# ax.hist(expScore, bins = 5, color = '#4E2A84')#histogram with Northwestern purple Go 'Cats
# ax.set_title('Visitors\' experience scores')

# # Route Score
# f,ax = plt.subplots(figsize = (8,5))
# ax.hist(routeScore, bins = 5, color = '#4E2A84')
# ax.set_title('Visitors\' experience scores')

# # Guide Score
# f,ax = plt.subplots(figsize = (8,5))
# ax.hist(guideScore, bins = 5, color = '#4E2A84')
# ax.set_title('Visitors\' experience scores')
