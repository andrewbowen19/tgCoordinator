# Feedback system for the tour guide program:
# Northwestern Univeristy Office of Undergraduate Admissions
# Segal Visitor's Center
# 1841 Hinman Ave, Evanston, IL, 60201
# Author: Andrew Bowen
# License: MIT License

"""New User script"""

import numpy as np
import pandas as pd
import tkinter as tk
# from tkinter.ttk import * # Maybe we should use more modern python GUIs
import bcrypt


# ####################################################################################
# Reading in TG master list data file
masterList = pd.read_csv('./../../data/Master-List.csv', header = 0, skiprows = [1])
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
# userDict = {guideEmails[i] : '' for i in range(len(masterList))}

# print(userDict)


# ############################################################################### # # # # # # # # # # #


class User(tk.Tk):
	'''Class for us to generate user profiles (username: email) for our tour guides, 

		want to store salted and hashed passwords in our dictionary
		'''

	def __init__(self):
		# self.master = tk.Tk.__init__(self)
		# self.entry = tk.Entry(self)
		# self.entry = tk.Entry(self)
		# self.button = tk.Button(self, text="Create User", command=self.createUser).grid(row=0, column=0, padx = 4, pady = 2)
		# self.button = tk.Button(self, text = 'Login', command = self.login).grid(row = 1, column = 0, padx =4 , pady = 2)
		self.userDict = dict()


	def on_button(self):
		# Fucntion that prints entry value when button is pushed
		print(self.entry.get())


	def addSaltedUser(self, username, password, dictionary):
		# Function that salts/hashes passwords and adds to userdict;

		hashed = bcrypt.hashpw(bytes(password, 'utf8'), bcrypt.gensalt())
		dictionary[username] = hashed

		print('username: ', username)
		print('new Dict with all the salt: ', dictionary)


	def createUser(self):
		self.master = tk.Tk()
		# Function to creat user profile and pass user infor to addUser function
		# Setting up entry fields in proper places
		e1 = tk.Entry(self.master).grid(row=0, column=1)
		e2 = tk.Entry(self.master).grid(row=1, column=1)
		e3 = tk.Entry(self.master).grid(row=2, column=1)

		tk.Label(self.master, text="Enter Email").grid(row=0)
		tk.Label(self.master, text="Enter password").grid(row=1)
		tk.Label(self.master, text="Confirm password").grid(row=2)

		email = e1.get()
		password = e2.get()
		confirmPass = e3.get()

		# Adding buttons to create user page
		tk.Button(self.master, text = 'Quit', command = self.quit).grid(row = 3, column =0)
		tk.Button(self.master, text = 'Create User', command = self.addSaltedUser(email, e2.get(), userDict)).grid(row=3, column=1)

		self.master.mainloop()

	def login(self):
		"""Function that allows guides to login"""
		self.master = tk.Tk()

		tk.Label(self.master, text="Enter Email").grid(row=0)
		tk.Label(self.master, text="Enter password").grid(row=1)
		# tk.Label(master, text="Confirm password").grid(row=2)

		e1 = tk.Entry(self.master)
		e2 = tk.Entry(self.master)

		e1.grid(row=0, column=1)
		e2.grid(row=1, column=1)

		tk.Button(self.master, text='Quit', command= self.on_button).grid(row=2, column=1)
		tk.Button(self.master, text='Enter', command= self.on_button).grid(row=2, column=1)

		self.master.mainloop()

		

	def runAll(self):
		self.createUser()
		self.login()

		


user = User()
user.runAll()
# user.mainloop()


# breakpoint()












