# Feedback system for the tour guide program:
# Northwestern Univeristy Office of Undergraduate Admissions
# Segal Visitor's Center
# 1841 Hinman Ave, Evanston, IL, 60201
# Author: Andrew Bowen
# License: MIT License

'''
Script to test out nltk python package
Want to incorporate sentiment analysis
tutorial here: https://www.digitalocean.com/community/tutorials/how-to-perform-sentiment-analysis-in-python-3-using-the-natural-language-toolkit-nltk
'''


from nltk.stem.wordnet import WordNetLemmatizer
from nltk.corpus import twitter_samples, stopwords
from nltk.tag import pos_tag
from nltk.tokenize import word_tokenize
from nltk import FreqDist, classify, NaiveBayesClassifier

import re, string, random
import pandas as pd

def remove_noise(tweet_tokens, stop_words = ()):
    '''
    Function to remove noise (words that don't contribute to meaning) from text

    '''
    cleaned_tokens = []

    for token, tag in pos_tag(tweet_tokens):
        token = re.sub('http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+#]|[!*\(\),]|'\
                       '(?:%[0-9a-fA-F][0-9a-fA-F]))+','', token)
        token = re.sub("(@[A-Za-z0-9_]+)","", token)

        if tag.startswith("NN"):
            pos = 'n'
        elif tag.startswith('VB'):
            pos = 'v'
        else:
            pos = 'a'

        lemmatizer = WordNetLemmatizer()
        token = lemmatizer.lemmatize(token, pos)

        if (len(token) > 0) and (token not in string.punctuation) and (token.lower() not in stop_words):
            cleaned_tokens.append(token.lower())
    return cleaned_tokens

def get_all_words(cleaned_tokens_list):
    for tokens in cleaned_tokens_list:
        for token in tokens:
            yield token

def get_tweets_for_model(cleaned_tokens_list):
    for tweet_tokens in cleaned_tokens_list:
        yield dict([token, True] for token in tweet_tokens)

def trainClassifier():
    '''
    Function to train model on classifying positive and negative comments
    
    '''
        # Positive and negative tweet lists
    positive_tweets = twitter_samples.strings('positive_tweets.json')
    negative_tweets = twitter_samples.strings('negative_tweets.json')
    text = twitter_samples.strings('tweets.20150430-223406.json')
    tweet_tokens = twitter_samples.tokenized('positive_tweets.json')#[0]

    stop_words = stopwords.words('english')

    positive_tweet_tokens = twitter_samples.tokenized('positive_tweets.json')
    negative_tweet_tokens = twitter_samples.tokenized('negative_tweets.json')
    # print('+/- tweets:  ', positive_tweet_tokens[0:10], negative_tweet_tokens[0:10])

    positive_cleaned_tokens_list = []
    negative_cleaned_tokens_list = []

    # Creating positive and negative tokens for tweets with noise removed
    for tokens in positive_tweet_tokens:
        positive_cleaned_tokens_list.append(remove_noise(tokens, stop_words))

    for tokens in negative_tweet_tokens:
        negative_cleaned_tokens_list.append(remove_noise(tokens, stop_words))

    all_pos_words = get_all_words(positive_cleaned_tokens_list) # part of speech words

    freq_dist_pos = FreqDist(all_pos_words)
    # print(freq_dist_pos.most_common(10))

    positive_tokens_for_model = get_tweets_for_model(positive_cleaned_tokens_list)
    negative_tokens_for_model = get_tweets_for_model(negative_cleaned_tokens_list)

    # Establishing positive and negative datasets from tokens
    positive_dataset = [(tweet_dict, "Positive")
                         for tweet_dict in positive_tokens_for_model]

    negative_dataset = [(tweet_dict, "Negative")
                         for tweet_dict in negative_tokens_for_model]

    # Creating randomized dataset
    dataset = positive_dataset + negative_dataset
    random.shuffle(dataset)

    # Establishing training and testing datasets
    train_data = dataset[:7000]
    test_data = dataset[7000:]
    # print(train_data[0:10], type(test_data))

    classifier = NaiveBayesClassifier.train(train_data) 

    print("Accuracy is:", classify.accuracy(classifier, test_data) * 100 ,'%')

    print(classifier.show_most_informative_features(10))

    return classifier
print('Training model to identify constructive feedback...')
# Calling trained model once - returns nltk Bayesian classifier object
model = trainClassifier()
# print('MODEL: ', model)

def classifyComment(comment, classifier):
    '''Function to use trained classifier above and apply to comments pulled from guide data'''

    custom_comment_tokens = remove_noise(word_tokenize(comment)) # Tour sample comment
    classification = model.classify(dict([token, True] for token in custom_comment_tokens))

    # Returngin either positive of negative classification
    return classification


# Reading in visitor feedback files (responses for every guide/tour)
indpath = '/Users/andrewbowen/tgCoordinator/data/indFiles/'
allpath = '/Users/andrewbowen/tgCoordinator/data/allFiles/'
feedback = pd.read_csv(allpath + 'Feedback_Form_Beta.csv', sep = ',', header = 0)

# Renaming the columns for easier readability
feedback.columns = ['Timestamp','Visitor Name', 'Visitor Email', 'Visitor Type', 'Visit Date', 'Guide Name',\
			'Exp Score', 'Route Score', 'Guide Score', 'Comments']

# Scores for plotting later
expScore = feedback['Exp Score']
guideScore = feedback['Guide Score']
routeScore = feedback['Route Score']

names = feedback['Guide Name']

guideName = input('Please input guide\'s name: ')
numComments = int(input('How many comments would you like to view? ')) # # of comments to display at end
# Pulling guide name data
guideData = feedback.loc[names == guideName]
good_comments = []



for comment in guideData['Comments']:
	comment_type = classifyComment(comment, model)
	print(comment, '--Result--> ', comment_type)

	# Grouping together positive comments
	if comment_type == 'Positive':
		good_comments.append(comment)

print('')
print('####################################')
print('')

# Displaying a few good comments
if numComments > len(guideData['Comments']):
    numComments = len(guideData['Comments'])
    print('There are fewer comments for that guide than you requested. Displaying what we can.')
print('Guide Feedback: ', good_comments[0: numComments])


# ## TODO: implement display of certain good comments

# Pseudo code:
# if comment_type = 'Postive':
# 	append to postive comment list
# 	show positive comment list (1-3 examples)

# 	Could ask user if they would like to see comments about something specifically








