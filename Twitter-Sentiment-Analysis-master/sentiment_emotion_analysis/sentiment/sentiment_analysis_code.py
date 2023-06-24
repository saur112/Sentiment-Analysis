import re
import nltk
from textblob import TextBlob
from nltk.stem.wordnet import WordNetLemmatizer
import emoji
from bs4 import BeautifulSoup
import itertools
import numpy as np
nltk.download('wordnet')



class sentiment_analysis_code():

    lem = WordNetLemmatizer()

    # def cleaning(self, text):
    #     txt = str(text)
    #     txt = re.sub(r"http\S+", "", txt)
    #     if len(txt) == 0:
    #         return 'no text'
    #     else:
    #         txt = txt.split()
    #         index = 0
    #         for j in range(len(txt)):
    #             if txt[j][0] == '@':
    #                 index = j
    #         txt = np.delete(txt, index)
    #         if len(txt) == 0:
    #             return 'no text'
    #         else:
    #             words = txt[0]
    #             for k in range(len(txt)-1):
    #                 words+= " " + txt[k+1]
    #             txt = words
    #             txt = re.sub(r'[^\w]', ' ', txt)
    #             if len(txt) == 0:
    #                 return 'no text'
    #             else:
    #                 txt = ''.join(''.join(s)[:2] for _, s in itertools.groupby(txt))
    #                 txt = txt.replace("'", "")
    #                 txt = nltk.tokenize.word_tokenize(txt)
    #                 #data.content[i] = [w for w in data.content[i] if not w in stopset]
    #                 for j in range(len(txt)):
    #                     txt[j] = self.lem.lemmatize(txt[j], "v")
    #                 if len(txt) == 0:
    #                     return 'no text'
    #                 else:
    #                     return txt
    def cleaning(self,a):
        a = re.sub('#bitcoin', 'bitcoin', a)
        a = re.sub('#Bitcoin', 'Bitcoin', a)
        a = re.sub('#Ethereum', 'Ethereum', a)
        a = emoji.demojize(a)
        a = a.replace(":", "")
        a = BeautifulSoup(a).get_text()
        a = re.sub('(#[A-Za-z0-9]+|@[A-Za-z0-9])', "", a)
        a = ' '.join(re.sub("[\.\,\!\?\:\;\-\=]", " ", a).split())
        a = re.sub('\\n', '', a)
        a = re.sub('\w+:\/\/\S+', '', a)
        # a = ' '.join(re.sub("(\w+:\/\/\S+)", " ", a).split())
        return a

    def get_tweet_sentiment(self, tweet):
        #cleaning of tweet
        if tweet:
            blob = TextBlob(tweet)
            # st.write('Polarity: ', round(blob.sentiment.polarity, 2))
            # st.write('Subjectivity: ', round(blob.sentiment.subjectivity, 2))
            tweet = ' '.join(self.cleaning(tweet))
            analysis = TextBlob(tweet)
            if round(blob.sentiment.polarity, 2)> 0:
                return [round(blob.sentiment.polarity, 2),'Positive']
            elif round(blob.sentiment.polarity, 2)== 0:
                return [round(blob.sentiment.polarity, 2),'Neutral']
            else:
                return [round(blob.sentiment.polarity, 2),'Negative']
    def get_tweet_sentiment_import(self, tweet):
        #cleaning of tweet
        if tweet:
            blob = TextBlob(tweet)
            # st.write('Polarity: ', round(blob.sentiment.polarity, 2))
            # st.write('Subjectivity: ', round(blob.sentiment.subjectivity, 2))
            tweet = ' '.join(self.cleaning(tweet))
            analysis = TextBlob(tweet)
            if round(blob.sentiment.polarity, 2)> 0:
                return 'Positive'
            elif round(blob.sentiment.polarity, 2)== 0:
                return 'Neutral'
            else:
                return 'Negative'