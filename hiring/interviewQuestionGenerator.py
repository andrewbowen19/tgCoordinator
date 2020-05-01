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
									'Arts on campus','School spirit','Location (Evanston/Chicago)'
				 ]

questions_hard = [
				 'North v. south?',
				 'I heard a ton of students are involved in greek life at Northwestern. Do you have to join a sorority or fraternity to have friends here?',
				 'Off campus living?', 
				 'Are students competitive or collaborative? Will I be competing with other students or working with them?',
				 "I got into Northwestern, but I was also accepted to Stanford and some Ivy League schools. Do Northwestern students ever feel like they're settling by coming here, or they're here just because they couldn't get into a better school?"
				 'I\'ve seen a lot of blue lights on campus. What\'s campus safety like? How can my daughter stay safe?',
				 'How do students spend their Friday and Saturday nights? Do students have fun here?', 
				 'How does Northwestern help prepare students for life after college?'
				 'I\'ve heard professors are inaccessible and classes can be taught by TAs? Why am I paying good money for a grad student to be teaching?',
				 'Does the quarter system put you at a disadvantage for summer internships? Do you feel like you\'re rushing through classes?',
				 'Are some majors harder than others?',
				 'No one from my high school has ever gone to Northwestern. Is it hard to adjust if you don\'t know anyone when you start?',
				 'Is it hard to get involved with research as a freshman?',
				 'Can you give an example of how the Northwestern community values diversity on campus (i.e. faculty, staff, administration, students, etc)',
				 'This is obviously a difficult school. How do students deal with stress? Does the quarter system exacerbate this?',
				 'Maintaining my mental health is a big worry for me as I go onto college. Have you found it difficult to maintain your mental health amidst college stresses? Does the fast paced quarter system make it harder? What are the mental health resources available to me on campus?',
				 'My family is concerned about the economic strain of attending college. How financially accessible have you found Northwestern, both in tuition and just in day-to-day life?',
				 'I\'m from California, and it gets pretty cold in Chicago. How does the campus community handle the weather? Will I like Northwestern even in the winter??',	



				 ] # Add more difficult question here

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

# def welcomeWindow():
# 		# Do once at beginning of interview
# 		form1 = sg.Window('Guide Interview')

# 		layout = [
# 							[sg.Text('Interviewer Name(s)', size=(15, 1)), sg.InputText('')],
# 							[sg.Text('# of Interviewees:', size=(15, 1)), sg.InputText('')],
# 							[sg.Text('Interviewee Name(s)', size=(15, 1)), sg.InputText('')],

# 							[sg.Submit(), sg.Cancel()]

# 						 ]
# 		button, values = form1.Layout(layout).Read()
# 		return button, values

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

		













