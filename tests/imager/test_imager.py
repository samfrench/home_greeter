from unittest import TestCase
from mock import Mock, call
from home_greeter.imager.imager import Imager

class TestImager(TestCase):
    def setUp(self):
        self.mock_classifier = Mock(autospec='home_greeter.imager.Classifier')
        self.mock_matcher    = Mock(autospec='home_greeter.imager.Matcher')
        self.imager          = Imager(classifier=self.mock_classifier, matcher=self.mock_matcher)

    def test_create(self):
        self.assertIsInstance(self.imager, Imager)

    def test_is_delivery(self):
        classifications = { 'car': 0.5 }

        with open(__file__, 'rb') as photo:
            self.mock_classifier.classify_image.return_value = classifications
            self.imager.is_delivery(photo)

        self.mock_classifier.classify_image.assert_called_once_with(photo)
        self.mock_matcher.is_delivery.assert_called_once_with(classifications)
