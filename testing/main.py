# Feedback system for the tour guide program:
# Northwestern Univeristy Office of Undergraduate Admissions
# 1841 Hinman Ave, Evanston, IL, 60201
# Author: Andrew Bowen
# License: MIT License

"""
Script to create a Python-based GUI for our guide feedback system
Will be interactive, modern GUI. Will integrate with our guide-feedback script
"""

import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# Importing stuff from kivy
# kivy documentation: https://kivy.org/doc/stable/guide/environment.html
import kivy
kivy.require('1.11.1')
from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput


# Reading in visitor feedback files (responses for every guide/tour)
indpath = '/Users/andrewbowen/tgCoordinator/data/indFiles/'
allpath = '/Users/andrewbowen/tgCoordinator/data/allFiles/'
feedback = pd.read_csv(allpath + 'Feedback_Form_Beta.csv', sep = ',',header = 0)

# Renaming the columns for easier readability
feedback.columns = ['Timestamp','Visitor Name', 'Visitor Email', 'Visitor Type', 'Visit Date', 'Guide Name',\
			'Exp Score', 'Route Score', 'Guide Score', 'Comments']


# Setting up initial search screen
class SearchScreen(GridLayout):

	def __init__(self, **kwargs):
		super(SearchScreen, self).__init__(**kwargs)

		self.cols = 2
		self.add_widget(Label(text='Guide First Name'))
		self.firstname = TextInput(multiline=False)
		self.add_widget(self.firstname)
		self.add_widget(Label(text='Guide Last Name'))
		self.lastname = TextInput(password=True, multiline=False)
		self.add_widget(self.lastname)


# Runs search screen
class MyApp(App):


    def build(self):
        return  SearchScreen()






if __name__ == '__main__':
    MyApp().run()












