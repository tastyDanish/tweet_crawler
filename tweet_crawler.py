import json
import numpy as np
import pandas as pd
import requests
from twitter import Twitter, OAuth, TwitterHTTPError, TwitterStream
import tweet_config

import tweepy
from tweepy import OAuthHandler

consumer_key = tweet_config.consumer_key
consumer_secret = tweet_config.consumer_secret

access_token = tweet_config.access_token
access_secret = tweet_config.access_secret


def stream_tweets():
    oauth = OAuth(access_token, access_secret, consumer_key, consumer_secret)

    twitter_stream = TwitterStream(auth=oauth)
    iterator = twitter_stream.statuses.sample()

    tweet_count = 5
    for tweet in iterator:
        tweet_count -= 1
        print(json.dumps(tweet))
        if tweet_count <= 0:
            break


def get_tweet_by_keyword(keyword):
    auth = OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_secret)
    api = tweepy.API(auth)

    max_tweets = 10
    searched_tweets = [status for status in tweepy.Cursor(api.search, q=keyword).items(max_tweets)]
    return searched_tweets


def get_trends():
    auth = OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_secret)
    api = tweepy.API(auth)
    return api.trends_place(2490383)


if __name__ == '__main__':
    trends = get_trends()
    for trend in trends:
        print(trend)