# Feedback system for the tour guide program:
# Northwestern Univeristy Office of Undergraduate Admissions
# 1841 Hinman Ave, Evanston, IL, 60201
# Author: Andrew Bowen
# License: MIT License

"""
Testing script to try to implement themed tkinter widgets
Want the widgets from our Search class to be themed, maybe NU purple?
"""

import numpy as np
import pandas as pd
import tkinter as tk

# Ussing themed tkinter widgets (ttk) to create more modern-looking GUIs
from tkinter import ttk
from tkinter.ttk import *

# Pulled from tkinter's theme documentation

style = ttk.Style()
style.configure("BW.TLabel", foreground="black", background="white")

l1 = ttk.Label(text="Test", style="BW.TLabel")
l2 = ttk.Label(text="Test", style="BW.TLabel")