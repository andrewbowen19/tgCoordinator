'''
Making a time series based on guide recs
'''

# Tour Guide Program : Feedback system
# Northwestern Univeristy Office of Undergraduate Admissions
# Segal Visitors' Center
# 1841 Hinman Ave, Evanston, IL, 60201
# Author: Andrew Bowen
# License: MIT License

import plotly.graph_objects as go
import numpy as np
import datetime

# plotly docs: https://plotly.com/python/


# Jacked from StackOverflow
# https://stackoverflow.com/questions/50165501/generate-random-list-of-timestamps-in-python
def randomtimes(start, end, n):
    frmt = '%d-%m-%Y %H:%M:%S'
    stime = datetime.datetime.strptime(start, frmt)
    etime = datetime.datetime.strptime(end, frmt)
    td = etime - stime
    return [np.random.random() * td + stime for _ in range(n)]


# Replace this fake data with generated 'time-series' data for a guide

guideName = 'Andrew Bowen'

# random dates - will pull from tour database later
tour_dates = sorted(randomtimes('9-10-2017 00:00:00', '4-4-2020 00:00:00', 25))
print('Sorted dates: ', tour_dates)

route_scores = np.array(np.random.randint(1, 5, 25))
exp_scores = np.array(np.random.randint(1, 5, 25))
guide_scores = np.array(np.random.randint(1, 5, 25))

print('scores: ', route_scores, exp_scores, guide_scores)

# Plotting route scores
fig = go.Figure(data=go.Scatter(x=tour_dates, y=route_scores))

fig.show()

# scatter plot - hover capability
# fig = px.scatter(df_2007, x="gdpPercap", y="lifeExp", log_x=True,
                 # hover_name="country", hover_data=["continent", "pop"])

# fig.show()

