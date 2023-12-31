from tweepy import OAuthHandler
from tweepy import API
from tweepy import Cursor
from datetime import datetime, date, time, timedelta
from collections import Counter
import sys
import tweepy
import numpy as np
import pandas as pd

class Import_tweet_emotion:

	consumer_key="b86rarCmDJAwfCZF49FTNzwxt"
	consumer_secret="qBwKbsVHfGpW9xuY1Jn1IG3b9Xipb6hHWSEapAEpEJkO2rfxWQ"
	access_token="1551961597903785984-wgvBdKJbHXeEFJmMt23RZ4P1Y8XX4C"
	access_token_secret="0obevQVW3QgyIPlkxAWJ4B5dz3SpgNZdEH3Tyuho3PFFI"

	def tweet_to_data_frame(self, tweets):
		df = pd.DataFrame(data=[tweet.text for tweet in tweets], columns=['Tweets'])
		return df

	def get_tweets(self, handle):
		auth = OAuthHandler(self.consumer_key, self.consumer_secret)
		auth.set_access_token(self.access_token, self.access_token_secret)
		auth_api = API(auth)

		account = handle
		item = auth_api.user_timeline(id=account,count=50)
		df = self.tweet_to_data_frame(item)

		all_tweets = []
		for j in range(50):
			all_tweets.append(df.loc[j]['Tweets'])
		return all_tweets

	def get_hashtag(self, hashtag):
		auth = OAuthHandler(self.consumer_key, self.consumer_secret)
		auth.set_access_token(self.access_token, self.access_token_secret)
		auth_api = API(auth)

		account = hashtag
		all_tweets = []

		for tweet in tweepy.Cursor(auth_api.search, q=account, lang='en').items(50):
			all_tweets.append(tweet.text)

		return all_tweets
