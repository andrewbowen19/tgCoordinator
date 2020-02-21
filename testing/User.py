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
# userDict = {guideEmails[i] : '' for i in range(len(masterList))}

# print(userDict)


# ############################################################################### # # # # # # # # # # #


class User(tk.Tk):
	'''Class for us to generate user profiles (username: email) for our tour guides, 

		want to store salted and hashed passwords in our dictionary
		'''

	def __init__(self):
		self.master = tk.Tk.__init__(self)
		self.entry = tk.Entry(self)
		self.entry = tk.Entry(self)
		self.button = tk.Button(self, text="Create User", command=self.createUser).grid(row=0, column=0, padx = 4, pady = 2)
		self.button = tk.Button(self, text = 'Login', command = self.login).grid(row = 1, column = 0, padx =4 , pady = 2)
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
		# Function to creat user profile and pass user infor to addUser function
		# Setting up entry fields in proper places
		e1 = tk.Entry(self).grid(row=0, column=1)
		e2 = tk.Entry(self).grid(row=1, column=1)
		e3 = tk.Entry(self).grid(row=2, column=1)

		tk.Label(self, text="Enter Email").grid(row=0)
		tk.Label(self, text="Enter password").grid(row=1)
		tk.Label(self, text="Confirm password").grid(row=2)

		# # Setting up entry fields
		# e1 = self.entry.grid(row=0, column=1)
		# e2 = self.entry.grid(row=1, column=1)
		# e3 = self.entry.grid(row=2, column=1)

		# test = self.entry.get()
		# print(test)
		# print('email & pass: ', userEmail, userPass)

		# Adding buttons to create user page
		tk.Button(self, text = 'Quit', command = self.quit).grid(row = 3, column =0)
		tk.Button(self, text = 'Create User', command = self.addSaltedUser(e1.get(), e2.get(), userDict)).grid(row=3, column=1)


		# self.mainloop()

	def login(self):
		"""Function that allows guides to login"""


		self.master = tk.Tk()

		tk.Label(self, text="Enter Email").grid(row=0)
		tk.Label(self, text="Enter password").grid(row=1)
		# tk.Label(master, text="Confirm password").grid(row=2)

		e1 = tk.Entry(self)
		e2 = tk.Entry(self)

		e1.grid(row=0, column=1)
		e2.grid(row=1, column=1)
		# e3.grid(row=2,column=1)

		# email = e1.get()

		tk.Button(self, text='Quit', command= self.on_button).grid(row=2, column=1)
		tk.Button(self, text='Enter', command= self.on_button).grid(row=2, column=1)

		

		# self.mainloop()
		# if email in self.userDict:

			# password = e2.get()
			# password = input('Please input your password: ')

			# Now check hashing password

			# if bcrypt.checkpw(password, self.userDict[email]):


			# If password entered is correct (using 1234 as test case)
			# if password == userDict[email]:
				# print('you in, homie')
			# 	return True
			# else:
			# 	return False

		# else:
		# 	print(False)
			# response = input('That email is not in our system, would you like to try again? [y/n]: ')
			# if 'n' in response or 'no' in response or 'N' in response:
			# 	return True
			# else:
			# 	return False
		self.master.mainloop()

	def runAll(self):
		self.createUser()
		self.login()

		


user = User()
# user.mainloop()


# breakpoint()












