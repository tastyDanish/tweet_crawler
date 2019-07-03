import json
import boto3
import tweepy
import tweet_config

consumer_key = tweet_config.consumer_key
consumer_secret = tweet_config.consumer_secret

access_token = tweet_config.access_token
access_secret = tweet_config.access_secret

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_secret)

kinesis_client = boto3.client('kinesis')


class MyStreamListener(tweepy.StreamListener):

    def on_status(self, status):
        print(status.text)

    def on_data(self, data):
        tweet = json.loads(data)
        print('Publishing record to the stream:', tweet)
        return True

    def on_error(self, status):
        print('ERROR: ' + str(status))


def main():
    my_stream_listener = MyStreamListener()
    my_stream = tweepy.Stream(auth=auth, listener=my_stream_listener)
    my_stream.filter(track=['#petertweetstreamtest'])


if __name__ == '__main__':
    main()
