# Feedback system for the tour guide program:
# Northwestern Univeristy Office of Undergraduate Admissions
# Segal Visitor's Center
# 1841 Hinman Ave, Evanston, IL, 60201
# Author: Andrew Bowen
# License: MIT License

'''
Script to generate hiring stats across all readers
Already hae plotting capability in 
'''

import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import matplotlib as mpl
from matplotlib import gridspec
import matplotlib.cm as cm
import os

path_to_data = '/Users/andrewbowen/tgCoordinator/hiring/data/'
data = pd.read_csv('./reader-scores.csv')


# renaming dtaframe columns 
new_names = ['Timestamp', 'Reader', 'Applicant ID #', 'Applicant ID # Confirm',
	 'Reader #', 'Appropriate', 'Campus Awareness', 'Originality', 'Thoroughness', 
	 'Campus Involvement', 'Video (Y/N)', 'Comments', 'Reasons for Concern', 'Schools', 'Majors']
data.columns = new_names

def hist2d():
	print('foo')
