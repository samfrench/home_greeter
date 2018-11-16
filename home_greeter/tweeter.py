import os
import tweepy

class Tweeter():
    def __init__(self, api=None):
        self.__api = api or self.__api()

    def tweet_message_with_image(self, message, image):
        status = self.__api.update_with_media(image, message)
        self.__api.update_status(status = message)

    def __api(self):
        consumer_key = os.getenv('TWITTER_CONSUMER_KEY')
        consumer_secret = os.getenv('TWITTER_CONSUMER_SECRET')
        access_token = os.getenv('TWITTER_ACCESS_TOKEN')
        access_token_secret = os.getenv('TWITTER_ACCESS_TOKEN_SECRET')
        auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
        auth.set_access_token(access_token, access_token_secret)
        api = tweepy.API(auth)
