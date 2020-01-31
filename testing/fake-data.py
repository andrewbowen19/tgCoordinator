# Feedback system for the tour guide program:
# Northwestern Univeristy Office of Undergraduate Admissions
# Segal Visitor's Center
# 1841 Hinman Ave, Evanston, IL, 60201
# Author: Andrew Bowen
# License: MIT License


"""Code to make fake test data for plotting
	Want to put new data into CSV files for read in later"""

import numpy as np
import pandas as pd

# Data frame to make into csv with test data
data = pd.DataFrame(columns = ['Timestamp','Visitor Name', 'Visitor Email', 'Visitor Type', 'Visit Date', 'Guide Name',\
			'Exp Score', 'Route Score', 'Guide Score', 'Comments'])

# data.columns = ['Timestamp','Visitor Name', 'Visitor Email', 'Visitor Type', 'Visit Date', 'Guide Name',\
# 			'Exp Score', 'Route Score', 'Guide Score', 'Comments']

guideNames = ['Andrew Bowen', 'Lauren Gold', 'Mia Lennon', 'Emily Coffee']

namesList = []

for i in range(0,500):
	index = np.random.randint(0,4)
	randGuide = guideNames[index]

	namesList.append(randGuide)


print(namesList)
# Test for guide, exp and route scores
exp  =  np.random.randint(0,6,500)
route = np.random.randint(0,6,500)
guide = np.random.randint(0,6,500)

print(exp)


data['Guide Name'] = namesList	
data['Exp Score'] = exp
data['Route Score'] = route
data['Guide Score'] = guide

print(data)

data.to_csv('./../data/plotting-data.csv', sep = ',')

