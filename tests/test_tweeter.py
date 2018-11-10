from unittest import TestCase
from mock import Mock, call, patch
from tests.mock_tweepy import MockTweepy
import tweepy
from home_greeter import Tweeter

class TestTweeter(TestCase):
    def setUp(self):
        self.mock_tweepy = Mock(autospec='tweepy')
        self.tweeter = Tweeter(api=self.mock_tweepy)

    def test_create(self):
        self.assertIsInstance(self.tweeter, Tweeter)

    def test_tweet_image(self):
        image_path = '/path/to/image.jpg'
        text = 'tweet'
        self.tweeter.tweet_image(image_path)
        self.mock_tweepy.assert_has_calls([
            call.update_with_media(image_path, text),
            call.update_status(status=text)
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
