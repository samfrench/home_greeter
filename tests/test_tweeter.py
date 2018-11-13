from unittest import TestCase
from mock import Mock, call, patch
from tests.mock_tweepy import MockTweepy
import tweepy
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

    @patch.object(tweepy, 'OAuthHandler')
    @patch.object(tweepy, 'API')
    def test_twitter_auth(self, api, auth):
        tweeter = Tweeter()
        auth.assert_has_calls([
            call('ck', 'cs'),
            call().set_access_token('at', 'ast')
        ])

        api.assert_called()
