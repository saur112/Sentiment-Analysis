import tweepy
from tweepy import OAuthHandler
from tweepy import API
from datetime import datetime, date, time, timedelta
from collections import Counter
import sys

import numpy as np
import pandas as pd

class Import_tweet_sentiment:

	consumer_key = "iBWCXvk6Hd58gHVDoB49aMX70"
	consumer_secret = "gZT6nlJ3roLl3YPxL2AM3xECyOniYLB0Dvbpvb3jWSf2rXnZpi"
	access_token = "1652202328936816640-nRxoO1frWI4M52VeXEekytDROcWHzs"
	access_token_secret = "wyX6ak1tU6SUG7lKN2pPJItBpgJuwtysfpZEdqqdDSgL2"

	def tweet_to_data_frame(self, tweets):
		# df = pd.DataFrame(data=[tweet.text for tweet in tweets], columns=['Tweets'])
		df=pd.read_csv(tweets)
		return df

	def get_tweets(self,df):
		# auth = OAuthHandler(self.consumer_key, self.consumer_secret)
		# auth.set_access_token(self.access_token, self.access_token_secret)
		# auth_api = API(auth)
		#
		# account = handle
		# item = auth_api.user_timeline(id=account,count=50)
		data=r"C:\Users\hp\Downloads\dataset_twitter-scraper-task_2023-05-08_16-02-25-423 (2).csv"
		# df=pd.read_csv(r"C:\Users\hp\Desktop\Book2.csv")
		# df = self.tweet_to_data_frame(data)
		all_tweets = []
		for j in range(35):
			all_tweets.append(df.loc[j]['tweet'])
		return all_tweets
	#
	def get_hashtag(self,df):
		# auth = OAuthHandler(self.consumer_key, self.consumer_secret)
		# auth.set_access_token(self.access_token, self.access_token_secret)
		# auth_api = API(auth)
		#
		# account = hashtag
		data = r"C:\Users\hp\Downloads\dataset_twitter-scraper-task_2023-05-08_16-02-25-423 (2).csv"
		# df = self.tweet_to_data_frame(data)
		# df=pd.read_csv(r"C:\Users\hp\Desktop\Book2.csv")
		all_tweets = []
		for j in range(35):
		# for tweet in tweepy.Cursor(auth_api.search_tweets, q=account, lang='en').items(50):
			all_tweets.append(df.loc[j]['tweet'])
		# print(all_tweets)
		return all_tweets
