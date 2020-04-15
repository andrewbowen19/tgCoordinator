# Feedback system for the tour guide program:
# Northwestern Univeristy Office of Undergraduate Admissions
# Segal Visitor's Center
# 1841 Hinman Ave, Evanston, IL, 60201
# Author: Andrew Bowen
# License: MIT License

'''
Script to test out nltk python package
Want to incorporate sentiment analysis
tutorial here:
https://www.digitalocean.com/community/tutorials/how-to-perform-sentiment-analysis-in-python-3-using-the-natural-language-toolkit-nltk
Rewriting this code as a class

for our demo with the project team
'''

import re
import string
import random
import pandas as pd
from nltk.stem.wordnet import WordNetLemmatizer
from nltk.corpus import twitter_samples
from nltk.corpus import stopwords
from nltk.tag import pos_tag
from nltk.tokenize import word_tokenize
from nltk import FreqDist
from nltk import classify
from nltk import NaiveBayesClassifier

class demoAnalyzer(object):
    '''
    Object to incorporate NLP into tour comment analysis
    Want to only call classifier once for training
    Then use the model for guide comments
    Currently using .JSON files
    Will want to rewrite guide comments to this format
    '''

    def __init__(self, guideName, comments):
        self.guideName = guideName
        self.comments = comments
        self.model = None

    def remove_noise(self, tweet_tokens, stop_words=()):
        '''
        Method to remove noise
        Removes words/characters that don\'t contribute to overall meaning'
        '''
        self.cleaned_tokens = []

        for token, tag in pos_tag(tweet_tokens):
            token = re.sub('http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+#]|[!*\(\),]|'
                           '(?:%[0-9a-fA-F][0-9a-fA-F]))+', '', token)
            token = re.sub("(@[A-Za-z0-9_]+)", "", token)

            if tag.startswith("NN"):
                pos = 'n'
            elif tag.startswith('VB'):
                pos = 'v'
            else:
                pos = 'a'

            lemmatizer = WordNetLemmatizer()
            token = lemmatizer.lemmatize(token, pos)

            if (len(token) > 0) and (token not in string.punctuation) and (token.lower() not in stop_words):
                self.cleaned_tokens.append(token.lower())
        return self.cleaned_tokens

    def get_all_words(self, cleaned_tokens_list):
        '''
        Method that gets words from cleaned tokens
        '''

        self.cleaned_tokens_list = cleaned_tokens_list
        for tokens in self.cleaned_tokens_list:
            for token in tokens:
                yield token

    def get_tweets_for_model(self, cleaned_tokens_list):
        '''Method to pull cleaned (noise removed tweets to apply to Model'''
        for tweet_tokens in cleaned_tokens_list:
            yield dict([token, True] for token in tweet_tokens)

    def trainClassifier(self):
        '''
        Method to train model on classifying positive and negative comment
        Would like to use actualy comments for the training data
        Need to convert those to a .JSON file structure
        '''
        print('Training model...')
        # Positive and negative tweet lists
        positive_tweets = twitter_samples.strings('positive_tweets.json')
        negative_tweets = twitter_samples.strings('negative_tweets.json')
        text = twitter_samples.strings('tweets.20150430-223406.json')
        tweet_tokens = twitter_samples.tokenized('positive_tweets.json')

        stop_words = stopwords.words('english')

        positive_tweet_tokens = twitter_samples.tokenized('positive_tweets.json')
        negative_tweet_tokens = twitter_samples.tokenized('negative_tweets.json')

        self.positive_cleaned_tokens_list = []
        self.negative_cleaned_tokens_list = []

        # Creating positive and negative tokens for tweets with noise removed
        for tokens in positive_tweet_tokens:
            self.positive_cleaned_tokens_list.append(self.remove_noise(tokens, stop_words))

        for tokens in negative_tweet_tokens:
            self.negative_cleaned_tokens_list.append(self.remove_noise(tokens, stop_words))

        # part of speech words
        self.all_pos_words = self.get_all_words(self.positive_cleaned_tokens_list)

        freq_dist_pos = FreqDist(self.all_pos_words)
        # print(freq_dist_pos.most_common(10))

        positive_tokens_for_model = self.get_tweets_for_model(self.positive_cleaned_tokens_list)
        negative_tokens_for_model = self.get_tweets_for_model(self.negative_cleaned_tokens_list)

        # Establishing positive and negative datasets from tokens
        positive_dataset = [(tweet_dict, "Positive")
                            for tweet_dict in positive_tokens_for_model]

        negative_dataset = [(tweet_dict, "Negative")
                            for tweet_dict in negative_tokens_for_model]

        # Creating randomized dataset
        self.dataset = positive_dataset + negative_dataset
        random.shuffle(self.dataset)

        # Establishing training and testing datasets
        train_data = self.dataset[:7000]
        test_data = self.dataset[7000:]
        # print(train_data[0:10], type(test_data))

        self.classifier = NaiveBayesClassifier.train(train_data)

        accuracy = classify.accuracy(self.classifier, test_data)
        print("Accuracy is:", accuracy * 100, '%')

        print(type(self.classifier.show_most_informative_features(10)))

        return self.classifier

    def establishModel(self):
        '''
        Method to be called once to train the model
        Will then use the model based off one training
        '''
        print('Establishing model to identify constructive feedback...')

        # Calling trained model once - returns nltk Bayes classifier object
        self.model = self.trainClassifier()



    def classifyComment(self, comment, classifier):
        '''
        Method to use trained classifier above
        Will apply to comments pulled from guide data
        '''

        self.comment = comment
        custom_comment_tokens = self.remove_noise(word_tokenize(self.comment))  # Tour sample comment

        # Might not want to train for every comment
        # self.model = self.trainClassifier()

        print('Creating comment classification...')
        self.classification = self.model.classify(dict([token, True]
                                                       for token in custom_comment_tokens))

        # Returning either positive of negative classification
        return self.classification

    def displayComments(self, guideName, comments, num):
        '''
        Method to display results of our model
        comments should be some sequence of comments
        will do this for any input of comments
        '''

        numComments = int(num)  # # of comments to display

        # List of positive comments to display later
        self.good_comments = []
        self.comments = comments

        for c in self.comments:
            comment_type = self.classifyComment(c, self.model)
            print(c, '--Result--> ', comment_type, '\n')
            # print('')

            # Grouping together positive comments
            if comment_type == 'Positive':
                self.good_comments.append(c)

        print('')
        print('####################################')
        print('')

        # Displaying a few good comments
        if numComments > len(comments):
            numComments = len(comments)
            print('There are fewer comments than you requested.')
        print('Guide Feedback: ', self.good_comments[0: numComments])


# ## TODO: testing and integration of this object into our django app


# Reading in visitor feedback files (responses for every guide/tour)
# allpath = '/Users/andrewbowen/tgCoordinator/data/allFiles/'
# feedback = pd.read_csv(allpath + 'Feedback_Form_Beta.csv', sep=',', header=0)

# # Renaming the columns for easier readability
# feedback.columns = ['Timestamp', 'Visitor Name', 'Visitor Email',
#                          'Visitor Type', 'Visit Date', 'Guide Name',
#                          'Exp Score', 'Route Score', 'Guide Score', 'Comments']

# names = feedback['Guide Name']
# guideName = input('Enter Guide Name: ')
# # Pulling guide name data
# guideData = feedback.loc[names == guideName]

# n = input('How many comments would you like to view? ')

# # comments = ['without a doubt, the lakefront views and the relaxed feeling from the tour guide\n', 'It was very informative and welcoming.\n', 'Great tour guide, awesome campus\n', "The tour guides really knew what they were talking about, and Skylar was really funny and personable. All the presenters I've seen at other schools weren't as fun as he was.\n", 'The guide actually allowed us into a classroom and let us have a dedicated question session, and the guide seemed much more genuine than the rest of my tour guides, especially in explaining why they chose Northwestern.\n', 'Once again I think the tour guides were not only extremely informative, but also shared with us their personal experiences, which gave us a different perspective of the school. Overall, great tour!\n', "My tour guide (I don't remember his name but he is a political science, history, and legal studies student from Colorado) was awesome  he took the time to answer everyone's specific questions and made me fall in love with the campus and community. He showed that he cares about the school and that he is proud to go there. This tour solidified Northwestern's place as my first-choice school.\n", "I feel Northwestern's tour made sure to create a welcoming, yet realistic view of the environment Northwestern holds.\n", 'I liked that the tour guide was very focused on personalizing the tour and answering all the questions asked. She did her best to keep the group engaged and I really liked how she spoke a lot about the different traditions around campus because I feel like a schools traditions is really one major thing that sets it apart from other schools for me. I also enjoyed how we got to spend times inside and out of buildings because I have felt that in many other tours I have been only shown the facade of different academic buildings, but on my tour at Northwestern I was shown the inside of various academic centers and I even got to see the commons and a typical classroom!\n', "The Northwestern tour stood out because of the tour's ability to allow the visitors to get a real taste of what going to Northwestern is really like! For example, we sat in a Northwestern classroom for part of the tour, which allowed me to think about my life if I were to attend this university.\n", 'We had a wonderful tour guide who had a ton of energy and enthusiasm. She was super encouraging and more than willing to answer any and all questions. Overall the visit was a fantastic experience!\n', "For most part showed nice overview of everything. However, didn't show dorms which was dissapointing\n","Nothing stands out, the tour guides were not great speakers. Perhaps better speech presenters are needed or study the skill in order to present the school at it's best. As a HS speech analyst, I'd say it was very hard to listen to them speak. They were over the top and almost silly.\n", 'It focused more on the arts than most other schools (likely because it has a bigger presence at your school than most). However, I wish we would have been shown more of the campus (we were only shown the southern third of campus). I also wish we were shown more of the academic buildings and were able to see inside.\n']

# # Test calling object above
# ca = demoAnalyzer(guideName, guideData['Comments']) #, comments)
# ca.establishModel()
# ca.displayComments(guideName, guideData['Comments'], n) #, comments)
