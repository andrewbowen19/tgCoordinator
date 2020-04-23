'''
Script to generate random questions for tour guide interviews
Want to have GUI that allows user to choose either harder or easier question
'''

import numpy as np
import PySimpleGUI as sg

# Questions lists
questions_easy = ['Food on campus', 'Living on campus',
									'Norris', 'Student groups', 'Athletics',
									'What are some learning opportunities outside the classroom?',
									'Favorite class? (and why)','Favorite campus tradition?',
									'Arts on campus','School spirit','Location (Evanston/Chicago)']

questions_hard = ['What are you doing after graduation you bum?', 'ooooh hard questions', 'yay tour guiding'] # Add more difficult question here

def randomQuestionGenerator():
		'''
		Function to generate random question from lists above, 
		should popup after intro screen (1 per interview)
		'''
		# Setting up GUI


		# button, values = form.Layout(layout).Read()
		# print('Button, values: ', button, values)
		keepGUI = True
		while keepGUI:
				form = sg.Window('Random Question Generator')  # begin with a blank form

				layout = [
							[sg.Button('Random Question 1 (Easier)')],
							[sg.Button('Random Question 2 (Tougher)')],
							[sg.Cancel()]
						 ]
				event, values = form.Layout(layout).Read()
				print('foo foo')
				# Random index to pick out questions
				i = np.random.randint(1, len(questions_easy))
				j = np.random.randint(1, len(questions_hard))

				if event == None or event == 'Cancel':
						keepGUI = False

				# Generate random Easy Question
				elif event == 'Random Question 1 (Easier)':
						result = sg.Popup(questions_easy[i])
						print(result)



				# Generate random Harder Question (#2)
				elif event == 'Random Question 2 (Tougher)':
						result = sg.Popup(questions_hard[j])

def welcomeWindow()
		# Do once at beginning of interview
		form1 = sg.Window('Guide Interview')

		layout = [
							[sg.Text('Interviewer Name(s)', size=(15, 1)), sg.InputText('')],
							[sg.Text('# of Interviewees:', size=(15, 1)), sg.InputText('')],
							[sg.Text('Interviewee Name(s)', size=(15, 1)), sg.InputText('')],

							[sg.Submit(), sg.Cancel()]

						 ]
		button, values = form1.Layout(layout).Read()
		return button, values

# # b, v = welcomeWindow()

# # generate questions
# if b == 'Submit':
#     randomQuestionGenerator()

# # Close out program
# elif b == 'Cancel':
#     form1.Close()

# welcomeWindow()

def listQuestionGenerator(interviewee_names):
		'''
		Function to map random questions to each interviewee
		Parameters: 
		interviewee_names: list of interviewee names
		'''
		numInterviewees = len(interviewee_names)

		i = np.random.randint(1, len(questions_easy))
		j = np.random.randint(1, len(questions_hard))

		



listQuestionGenerator(['Mary', 'Tyler', 'Chad'])

		













