# Feedback system for the tour guide program:
# Northwestern Univeristy Office of Undergraduate Admissions
# Segal Visitor's Center
# 1841 Hinman Ave, Evanston, IL, 60201
# Author: Andrew Bowen
# License: MIT License

'''
Script to convert csv comment files to .JSON file
'''

import json
import pandas as pd
import csv

csvFilePath = 'nu-survey-responses-examples.csv'
jsonFilePathPositive = 'tour_comments.json'

positive_comments = []
negative_comments = []

data = {}

n = 0
with open(csvFilePath, errors='ignore') as csvFile:
	csvReader = csv.reader(csvFile)
	for row in csvReader:
		n += 1
		print(row)

		# Classifying comments by hand
		classification_by_hand = input('Positive or negative?[p/n]: ')
		if 'p' in classification_by_hand or 'P' in classification_by_hand:
			positive_comments.append(row[0])

		if 'n' in classification_by_hand or 'N' in classification_by_hand:
			negative_comments.append(row[0])

		if 'foo' in classification_by_hand:
			break


print(positive_comments)
# print(data)

with open('positive-comments.txt', 'w') as f:
	for c in positive_comments:
		f.write(c)


with open('positive-comments.txt', 'w') as f:
	for c in negative_comments:
		f.write(c)





# writing to a json file
# with open(jsonFilePath, 'w') as jsonFile:
# 	jsonFile.write(json.dumps(data, indent=4))











