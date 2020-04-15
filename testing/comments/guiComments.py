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
# from commentAnalyzer import commentAnalyzer
from demoAnalyzer import demoAnalyzer

form = sg.FlexForm('Simple comment entry form')  # begin with a blank form

layout = [
          [sg.Text('Please enter your Name')],
          [sg.Text('Guide Name', size=(15, 1)), sg.InputText('')],
          [sg.Text('# Comments', size=(15, 1)), sg.InputText('')],
          # [sg.Text('Date', size=(15, 1)), sg.InputText('Date')],
          [sg.Submit(), sg.Cancel()]
         ]

button, values = form.Layout(layout).Read()

print(button, values[0])  #, values[1], values[2])


# # Calling class
# ca = commentAnalyzer(values[0])
# ca.displayComments(values[0])

# sg.Popup(ca, values[0])
# Reading in visitor feedback files (responses for every guide/tour)
allpath = '/Users/andrewbowen/tgCoordinator/data/allFiles/'
feedback = pd.read_csv(allpath + 'Feedback_Form_Beta.csv', sep=',', header=0)

# Renaming the columns for easier readability
feedback.columns = ['Timestamp', 'Visitor Name', 'Visitor Email',
                         'Visitor Type', 'Visit Date', 'Guide Name',
                         'Exp Score', 'Route Score', 'Guide Score', 'Comments']

names = feedback['Guide Name']

# Pulling guide name data
guideData = feedback.loc[names == values[0]]


ca = demoAnalyzer(values[0], guideData['Comments']) #, comments)
ca.establishModel()
ca.displayComments(values[0], guideData['Comments'], values[1])

# Closing window and posting constructive comments
form.close()

result = sg.Popup(values[0], ca.good_comments)





