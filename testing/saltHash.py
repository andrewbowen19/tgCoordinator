# Feedback system for the tour guide program:
# Northwestern Univeristy Office of Undergraduate Admissions
# Segal Visitor's Center
# 1841 Hinman Ave, Evanston, IL, 60201
# Author: Andrew Bowen
# License: MIT License

'''Test script for salting/hashing passwords from tour guide users'''

import numpy as np
import pandas as pd
import tkinter as tk
from tkinter.ttk import * # Maybe we should use more modern python GUIs
import bcrypt

# import string
# import random

# def randomString(stringLength=10):
#     """Generate a random string of fixed length """
#     letters = string.ascii_lowercase
#     return b''.join(random.choice(letters) for i in range(stringLength))

passwords = [b'123456' for i in range(100)]


for word in passwords:
	hashed = bcrypt.hashpw(word, bcrypt.gensalt())

	print(hashed)

	if bcrypt.checkpw(word, hashed):
		print("It Matches!")
	else:
	    print("It Does not Match :(")