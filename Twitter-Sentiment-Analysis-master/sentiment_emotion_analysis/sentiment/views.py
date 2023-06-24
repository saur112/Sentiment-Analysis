from django.shortcuts import render, redirect, HttpResponse
from .forms import Sentiment_Typed_Tweet_analyse_form
from .sentiment_analysis_code import sentiment_analysis_code
from .forms import Sentiment_Imported_Tweet_analyse_form
from .tweepy_sentiment import Import_tweet_sentiment
import pandas as pd


def sentiment_analysis(request):
    return render(request, 'home/sentiment.html')

def sentiment_analysis_type(request):
    if request.method == 'POST':
        form = Sentiment_Typed_Tweet_analyse_form(request.POST)
        analyse = sentiment_analysis_code()
        if form.is_valid():
            tweet = form.cleaned_data['sentiment_typed_tweet']
            sentiment = analyse.get_tweet_sentiment(tweet)
            args = {'tweet':tweet, 'polarity':sentiment[0],'sentiment':sentiment[1]}
            return render(request, 'home/sentiment_type_result.html', args)

    else:
        form = Sentiment_Typed_Tweet_analyse_form()
        return render(request, 'home/sentiment_type.html')

def sentiment_analysis_import(request):
    if request.method == 'POST':
        form = Sentiment_Imported_Tweet_analyse_form(request.POST)
        tweet_text = Import_tweet_sentiment()
        analyse = sentiment_analysis_code()

        if form.is_valid():
            handle = form.cleaned_data['sentiment_imported_tweet']

            if handle[0]=='#':
                df = pd.read_csv(r"C:\Users\hp\Desktop\bitcointweetsscraping.csv")
                list_of_tweets = tweet_text.get_hashtag(df)
                list_of_tweets_and_sentiments = []
                for i in list_of_tweets:
                    list_of_tweets_and_sentiments.append((i,analyse.get_tweet_sentiment_import(i)))
                args = {'list_of_tweets_and_sentiments':list_of_tweets_and_sentiments, 'handle':handle}
                return render(request, 'home/sentiment_import_result_hashtag.html', args)

            if handle[0]=='@elonmusk':
                df = pd.read_csv(r"C:\Users\hp\Desktop\elon_tweets.csv")
                list_of_tweets = tweet_text.get_tweets(df)
                list_of_tweets_and_sentiments = []
                if handle[0]!='@':
                    handle = str('@'+handle)
                for i in list_of_tweets:
                    list_of_tweets_and_sentiments.append((i,analyse.get_tweet_sentiment_import(i)))
                args = {'list_of_tweets_and_sentiments':list_of_tweets_and_sentiments, 'handle':handle}
                return render(request, 'home/sentiment_import_result.html', args)

            if handle=='random_tweet':
                df = pd.read_csv(r"C:\Users\hp\Desktop\train_tweet.csv")
                list_of_tweets = tweet_text.get_tweets(df)
                list_of_tweets_and_sentiments = []
                # if handle[0]!='@':
                #     handle = str('@'+handle)
                for i in list_of_tweets:
                    list_of_tweets_and_sentiments.append((i,analyse.get_tweet_sentiment_import(i)))
                args = {'list_of_tweets_and_sentiments':list_of_tweets_and_sentiments, 'handle':handle}
                return render(request, 'home/sentiment_import_result.html', args)
            if handle=='@crypto':
                df = pd.read_csv(r"C:\Users\hp\Desktop\crypto.csv")
                list_of_tweets = tweet_text.get_tweets(df)
                list_of_tweets_and_sentiments = []
                if handle[0]!='@':
                    handle = str('@'+handle)
                for i in list_of_tweets:
                    list_of_tweets_and_sentiments.append((i,analyse.get_tweet_sentiment_import(i)))
                args = {'list_of_tweets_and_sentiments':list_of_tweets_and_sentiments, 'handle':handle}
                return render(request, 'home/sentiment_import_result.html', args)

    else:
        form = Sentiment_Imported_Tweet_analyse_form()
        return render(request, 'home/sentiment_import.html')
