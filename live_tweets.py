import datetime
import os
from dotenv import load_dotenv
import tweepy
#from tweepy import OAuthHandler
#import time

load_dotenv('.env')
bearer_token = os.environ.get("BEARER_TOKEN")

class Listener(tweepy.StreamingClient):
    def on_connect(self):
        print('connected')

#     # def on_includes(self, includes):
#     #     self.tweets["username"] = includes['users'][0].username
#     #     print(self.tweets)
#
    def on_tweet(self, tweet):
        tweet_created_time = tweet.created_at + datetime.timedelta(hours=5)
        print("Tweet: ", tweet.text)
        time_diff = datetime.datetime.timestamp(datetime.datetime.now()) - datetime.datetime.timestamp(tweet.created_at)
        print("Tweet Stream Time: ", datetime.datetime.now())
        print("Tweet Created Time: ", tweet_created_time)
        print("Difference", time_diff)
        #self.tweets.append(tweet.text)
        #print(tweet.data)

twitter_profile_name = "moiz3297"

stream_tweet = Listener(bearer_token=bearer_token)
stream_tweet.add_rules(tweepy.StreamRule('from:' + twitter_profile_name))

stream_tweet.filter(tweet_fields=['created_at', 'lang'])

