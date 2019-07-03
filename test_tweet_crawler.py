import unittest
import tweet_crawler


class TestApp(unittest.TestCase):

    def test_get_tokens(self):
        consumer_key, consumer_secret, access_token, access_secret = tweet_crawler.get_tokens()

        print(consumer_key)
        print(consumer_secret)
        print(access_token)
        print(access_secret)

    def test_get_trending(self):
        trending = tweet_crawler.get_trends()
        print(trending)