# Feedback system for the tour guide program:
# Northwestern Univeristy Office of Undergraduate Admissions
# Segal Visitor's Center
# 1841 Hinman Ave, Evanston, IL, 60201
# Author: Andrew Bowen
# License: MIT License

'''
GUI script for our demo at the project meeting
'''

import PySimpleGUI as sg
import numpy as np
import pandas as pd
from commentAnalyzer import commentAnalyzer

form = sg.FlexForm('Simple comment entry form')  # begin with a blank form

layout = [
          [sg.Text('Please enter your Name')],
          [sg.Text('Guide Name', size=(15, 1)), sg.InputText('')],
          # [sg.Text('Comment on Tour', size=(15, 1)), sg.InputText('Comment')],
          # [sg.Text('Date', size=(15, 1)), sg.InputText('Date')],
          [sg.Submit(), sg.Cancel()]
         ]

button, values = form.Layout(layout).Read()

print(button, values[0])  #, values[1], values[2])


# Calling class
ca = commentAnalyzer(values[0])
ca.displayComments(values[0])


