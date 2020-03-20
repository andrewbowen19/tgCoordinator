# Feedback system for the tour guide program:
# Northwestern Univeristy Office of Undergraduate Admissions
# Segal Visitor's Center
# 1841 Hinman Ave, Evanston, IL, 60201
# Author: Andrew Bowen
# License: MIT License

'''New user script'''


# Let's make this work


import numpy as np
import pandas as pd
import tkinter as tk
# from tkinter.ttk import * # Maybe we should use more modern python GUIs
import bcrypt


# ####################################################################################
# Reading in TG master list data file
masterList = pd.read_csv('./../../data/Master-List.csv', header = 0, skiprows = [1])
guideEmails = masterList['Email']

# Fixing Name issue with dataframe from master list (originally listed in separate 'First' & 'Last columns')
firstName = masterList['First Name']
lastName = masterList['Last Name']

names = []
for first, last in zip(firstName, lastName):
	fullName = first + ' ' + last

	names.append(fullName)

print(names, guideEmails)

userDict = dict() #dictionary that creates 

def addUser(email, password, confirm):

	if password == confirm:
		hashed = bcrypt.hashpw(bytes(password, 'utf8'), bcrypt.gensalt())
		userDict[email] = hashed
		print('User Account created!')
		print('Current userbase: ',userDict)





# #################################################
# Creating GUI - 'Create User'
master = tk.Tk()

tk.Label(master, text="Enter Email").grid(row=0)
tk.Label(master, text="Enter password").grid(row=1)
tk.Label(master, text="Confirm password").grid(row=2)

e1 = tk.Entry(master)#.grid(row=0, column=1)
e2 = tk.Entry(master)#.grid(row=1, column=1)
e3 = tk.Entry(master)#.grid(row=2, column=1)

e1.grid(row=0, column=1)
e2.grid(row=1, column=1)
e3.grid(row=2, column=1)


# Getting text from entrys -- WHY ARE YOU NOT WORKING YOU GARBAGE???
email = e1.get()
password = e2.get()
confirmPass = e3.get()

# Adding buttons to create user page
QuitButton = tk.Button(master, text = 'Quit', command = quit)#.grid(row = 3, column =0)
createUserButton = tk.Button(master, text = 'Create User', command = addUser(email, password, confirmPass))#.grid(row=3, column=1)

QuitButton.grid(row = 3, column =0)
createUserButton.grid(row = 3, column =1)


master.mainloop()




