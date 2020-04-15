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

class commentAnalyzer(object):
    '''
    Object to incorporate NLP into tour comment analysis
    Want to only call classifier once for training
    Then use the model for guide comments
    Currently using .JSON files
    Will want to rewrite guide comments to this format
    '''

    def __init__(self, guideName):
        self.guideName = guideName
        # self.comment = comment
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

        print(self.classifier.show_most_informative_features(10))

        return self.classifier

    # def establishModel(self):
    #     print('Training model to identify constructive feedback...')
    #     # Calling trained model once - returns nltk Bayes classifier object
    #     self.model = self.trainClassifier()
    #     # return self.model
    

    def classifyComment(self, comment, classifier):
        '''
        Method to use trained classifier above
        Will apply to comments pulled from guide data
        '''

        self.comment = comment
        custom_comment_tokens = self.remove_noise(word_tokenize(self.comment))  # Tour sample comment

        # Might not want to train for every comment
        self.model = self.trainClassifier()

        print('Creating comment classification...')
        self.classification = self.model.classify(dict([token, True]
                                                       for token in custom_comment_tokens))

        # Returngin either positive of negative classification
        return self.classification

    def displayComments(self, guideName):

        # Reading in visitor feedback files (responses for every guide/tour)
        allpath = '/Users/andrewbowen/tgCoordinator/data/allFiles/'
        self.feedback = pd.read_csv(allpath + 'Feedback_Form_Beta.csv', sep=',', header=0)

        # Renaming the columns for easier readability
        self.feedback.columns = ['Timestamp', 'Visitor Name', 'Visitor Email',
                                 'Visitor Type', 'Visit Date', 'Guide Name',
                                 'Exp Score', 'Route Score', 'Guide Score', 'Comments']

        self.names = self.feedback['Guide Name']

        numComments = 2  # # of comments to display
        # Pulling guide name data
        self.guideData = self.feedback.loc[self.names == self.guideName]
        good_comments = []

        # ca = commentAnalyzer(guideName)

        for comment in self.guideData['Comments']:
            comment_type = self.classifyComment(comment, self.model)
            print(comment, '--Result--> ', comment_type)

            # Grouping together positive comments
            if comment_type == 'Positive':
                good_comments.append(comment)

        print('')
        print('####################################')
        print('')

        # Displaying a few good comments
        if numComments > len(self.guideData['Comments']):
            numComments = len(self.guideData['Comments'])
            print('There are fewer comments than you requested.')
        print('Guide Feedback: ', good_comments[0: numComments])


# ## TODO: testing and integration of this object into our django app

# Test calling object above
ca = commentAnalyzer('Lauren Gold')
ca.displayComments('Andrew Bowen')
