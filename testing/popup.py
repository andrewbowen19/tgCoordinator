# Feedback system for the tour guide program:
# Northwestern Univeristy Office of Undergraduate Admissions
# 1841 Hinman Ave, Evanston, IL, 60201
# Author: Andrew Bowen
# License: MIT License

'''
Script to create popup window for our guide name-entry feedback system
 uses Tkinter python package to create popup windows

'''

# Source code for some of this: https://www.python-course.eu/tkinter_entry_widgets.php
# Check for any easier means ofdoing this (maybe there's some method in JavaScript?)
# import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import tkinter as tk
# Ussing themed tkinter widgets (ttk) to create more modern-looking GUIs
from tkinter.ttk import *




master = tk.Tk()
tk.Label(master, text="Guide First Name").grid(row=0)
tk.Label(master, text="Last Name").grid(row=1)

e1 = tk.Entry(master)
e2 = tk.Entry(master)
e3 = tk.Entry(master)

firstName = e1.grid(row=0, column=1)
lastName = e2.grid(row=1, column=1)


# Stuff to add buttons
def show_entry_fields():
	"""Function to call for our """

	print("First Name: %s\nLast Name: %s" % (e1.get(), e2.get()))
	import matplotlib.pyplot as plt
	x = np.random.random(100)
	y = np.random.random(100)
	GuideName = e1.get() + ' ' + e2.get()
	f,ax = plt.subplots()
	ax.scatter(x,y)
	ax.set_title(GuideName)
	plt.show()


# Setting up input buttons on entry widget
tk.Button(master, text='Quit', command=master.quit).grid(row=3, column=0, sticky=tk.W, pady=4)
tk.Button(master, text='View Feedback', command=show_entry_fields).grid(row=3, column=1, sticky=tk.W, padx = 5,pady=5)



master.mainloop()


# # This works to create a popup menu, check later to see if it can be sleeker/do more stuff

# guideName = e1.get() + e2.get()
# scat = randomScat(guideName)















