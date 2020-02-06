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
import bcrypt


# ####################################################################################
# Reading in TG master list data file
masterList = pd.read_csv('./../data/Master-List.csv', header = 0, skiprows = [1])
guideEmails = masterList['Email']

# ####################################################################################

# Fixing Name issue with dataframe from master list (originally listed in separate 'First' & 'Last columns')
firstName = masterList['First Name']
lastName = masterList['Last Name']

names = []
for first, last in zip(firstName, lastName):
	fullName = first + ' ' + last

	names.append(fullName)
# ###################################################

# Need to have every guide provide their own password/PIN #
# Making passwords feault ot 1234 until we send out a Google sheet
# passwords = ['1234' for x in range(len(guideEmails))]

# Now we want to create a dictionary from our emails list and our password list (maybe names too)
userDict = {guideEmails[i] : '' for i in range(len(masterList))}

print(userDict)


# ############################################################################### # # # # # # # # # # #

# Need to salt and hash passwords - testing out bcrypt


def createUser():
	'''Function to create user profiles - may want to ingerate with our GUI
		(look up stuff that isn\'t tkinter) - python has nothing :)'''

	# creating tkinter widget
	master = tk.Tk()

	# Adding buttons to create user page
	tk.Button(master, text = 'Quit', command = master.quit).grid(row = 3, column =0)
	tk.Button(master, text = 'Create User', command = master.home).grid(row=3, column=1)

	tk.Label(master, text="Enter Email").grid(row=0)
	tk.Label(master, text="Enter password").grid(row=1)
	tk.Label(master, text="Confirm password").grid(row=2)

	e1 = tk.Entry(master)
	e2 = tk.Entry(master)
	e3 = tk.Entry(master)


	e1.grid(row=0, column=1)
	e2.grid(row=1, column=1)
	e3.grid(row=2,column=1)

	userEmail = e1.get()
	userPass = e2.get()
	confirmPass = e3.get()

	# userEmail = input('What is your NU email?: ')
	# userPass = input('Please input a password: ')
	# confirmPass = input('Please re-enter your password for confirmation: ')

	# Password confirmation
	if userPass == confirmPass:
		print('Welcome, fam')

		# Now we salt and hash the passwords using bcrypt -- DO NOT STORE USER PASSWORDS IN PLAINTEXT!!!
		userPass = bytes(userPass, 'utf8') # need to convert passwords to bytes for bcrypt
		hashed = bcrypt.hashpw(userPass, bcrypt.gensalt())
		userDict[userEmail] = hashed
		print('new user dict: ', userDict)

		# Can check if hashed password and raw password match
		# if bcrypt.checkpw(userPass, hashed):
		# 	print("It Matches!")
		# else:
		# 	print("It Does not Match :(")

		# User hashed passwords aded to our dictionaries

	else:
		print('The passwords provided do not match.')



def login():
	"""Function that allows guides to login"""
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




# #############################################################################################

# Below if Tkinter GUI stuff, we may go more modern (Qt or PyQt)
master = tk.Tk()

loginButton = tk.Button(master, text = 'Login', command = login).grid(row=0, column=0, sticky=tk.W, pady=4)
createAccountButton = tk.Button(master, text = 'Create Account', command = createUser).grid(row=1, column=0, sticky=tk.W, pady=4)


e1 = tk.Entry(master)
e2 = tk.Entry(master)
e3 = tk.Entry(master)
master.mainloop()

# createUser()


# while loop to keep program running, let's avoid infinite loops
# user = False
# n = 0
# while user == False and n < 3:
# 	user = login()
# 	n += 1


# #########################################################################################################

# Trying out PyQt widgets































