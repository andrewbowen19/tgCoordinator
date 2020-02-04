# Feedback system for the tour guide program:
# Northwestern Univeristy Office of Undergraduate Admissions
# Segal Visitor's Center
# 1841 Hinman Ave, Evanston, IL, 60201
# Author: Andrew Bowen
# License: MIT License

"""Script for us to test out different login methods"""

import numpy as np
import pandas as pd
import tkinter as tk
from tkinter.ttk import * # Maybe we should use more modern python GUIs

# ####################################################################################

masterList = pd.read_csv('./../data/Master-List.csv', header = 0, skiprows = [1])
guideEmails = masterList['Email']

# Fixing Name issue with dataframe from master list (originally listed in separate 'First' & 'Last columns')
firstName = masterList['First Name']
lastName = masterList['Last Name']


names = []
for first, last in zip(firstName, lastName):
	fullName = first + ' ' + last

	names.append(fullName)


# Need to have every guide provide their own password/PIN #
# Making passwords feault ot 1234 until we send out a Google sheet
passwords = ['1234' for x in range(len(guideEmails))]

# Now we want to create a dictionary from our emails list and our password list (maybe names too)

userDict = {guideEmails[i]: passwords[i] for i in range(len(passwords))}




# ############################################################################### # # # # # # # # # # #

def createUser():
	"""Function to take user-given email and select guide from list"""
	email = input('What is your email: ')
	if email in userDict:

		password = input('Please input your password: ')

		# If password entered is correct (using 1234 as test case)
		if password == userDict[email]:
			print('you in, homie')
			return True
		else:
			return False

	else:
		response = input('That email is not in our system, would you like to try again? [y/n]: ')
		if 'n' in response or 'no' in response or 'N' in response:
			return True
		else:
			return False



# while loop to keep program running, let's avoid infinite loops
user = False
n = 0
while user == False and n < 3:
	user = createUser()
	n += 1





