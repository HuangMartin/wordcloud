from tabnanny import process_tokens
import tweepy
import numpy as np
import configparser
import pandas as pd
import matplotlib.pylab as plt
from wordcloud import STOPWORDS, WordCloud
import wordcloud

#read config.ini(twitter api key.secret)
config = configparser.ConfigParser()
config.read('config.ini')

api_key = config['twitter']['api_key']
api_key_secret = config['twitter']['api_key_secret']
access_token = config['twitter']['access_token']
access_token_secret = config['twitter']['access_token_secret']

# authentication
auth = tweepy.OAuth1UserHandler(api_key, api_key_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)

#catch user tweets
user = 'elonmusk'
limit = 300
tweets = tweepy.Cursor(api.user_timeline, screen_name=user, 
    count=200, tweet_mode='extended').items(limit)

#create DataFrame
columns = ['User', 'Tweet']
data = []
for tweet in tweets:
    data.append([tweet.user.screen_name, tweet.full_text])
df = pd.DataFrame(data, columns=columns)

#將user tweets save as csv
df.to_csv('tweets.csv')

# read csv
data_file = pd.read_csv('tweets.csv')


#個人主頁
# public_tweets = api.home_timeline()
# for tweet in public_tweets:
#     print(tweet.text)

#印出指定用戶twitter ID & bio簡介
#user = api.get_user(screen_name="elonmusk")
#print(user.name)
#print(user.description)