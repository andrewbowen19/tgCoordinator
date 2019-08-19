# Feedback system for the tour guide program:
# Northwestern Univeristy Office of Undergraduate Admissions
# 1841 Hinman Ave, Evanston, IL, 60201
# Author: Andrew Bowen

'''
Script to create popup window for our guide name-entry feedback system
 uses Tkinter python package to create popup windows

'''

# Source code for some of this: https://www.python-course.eu/tkinter_entry_widgets.php
# Check for any easier means ofdoing this (maybe there's some method in JavaScript?)

import pandas as pd
import tkinter as tk

master = tk.Tk()
tk.Label(master, text="Guide First Name").grid(row=0)
tk.Label(master, text="Last Name").grid(row=1)

e1 = tk.Entry(master)
e2 = tk.Entry(master)
e3 = tk.Entry(master)

e1.grid(row=0, column=1)
e2.grid(row=1, column=1)

master.mainloop()


# This works to create a popup menu, check later to see if it can be sleeker/do more stuff