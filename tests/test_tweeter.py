from unittest import TestCase
from mock import Mock, call, patch
import os
from home_greeter.tweeter import Tweeter

class TestTweeter(TestCase):
    def setUp(self):
        self.mock_tweepy = Mock(autospec='tweepy')
        self.tweeter = Tweeter(api=self.mock_tweepy)

    def test_create(self):
        self.assertIsInstance(self.tweeter, Tweeter)

    def test_tweet_image(self):
        image = '/path/to/image.jpg'
        message = 'tweet'
        self.tweeter.tweet_message_with_image(message, image)
        self.mock_tweepy.assert_has_calls([
            call.update_with_media(image, message),
            call.update_status(status=message)
        ])

    @patch('tweepy.OAuthHandler')
    @patch('tweepy.API')
    def test_twitter_auth(self, api, auth):
        tweeter = Tweeter()
        auth.assert_has_calls([
            call(os.getenv('TWITTER_CONSUMER_KEY'), os.getenv('TWITTER_CONSUMER_SECRET')),
            call().set_access_token(os.getenv('TWITTER_ACCESS_TOKEN'), os.getenv('TWITTER_ACCESS_TOKEN_SECRET'))
        ])

        api.assert_called()
