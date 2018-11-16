from unittest import TestCase
from mock import Mock
from home_greeter.imager.matcher import Matcher

class TestImager(TestCase):
    def setUp(self):
        self.matcher = Matcher()

    def test_create(self):
        self.assertIsInstance(self.matcher, Matcher)

    def test_is_delivery_all_words_matching(self):
        classifications = { 'parcel': 0.9999243, 'package': 0.9999243, 'delivery': 0.9999243 }
        self.assertTrue(self.matcher.is_delivery(classifications))

    def test_is_delivery_one_word_matching(self):
        classifications = { 'parcel': 0.9999243, 'person': 0.9999243, 'door': 0.9999243 }
        self.assertTrue(self.matcher.is_delivery(classifications))

    def test_is_delivery_no_words_matching(self):
        classifications = { 'tree': 0.9999243, 'person': 0.9999243, 'door': 0.9999243 }
        self.assertFalse(self.matcher.is_delivery(classifications))

    def test_is_delivery_no_words_to_match(self):
        classifications = {}
        self.assertFalse(self.matcher.is_delivery(classifications))

    def test_is_delivery_and_concept_value_lower_than_threshold(self):
        classifications = { 'parcel': 0.8999243, 'package': 0.7999243, 'delivery': 0.6999243 }
        self.assertFalse(self.matcher.is_delivery(classifications))

    def test_is_delivery_and_one_concept_value_lower_than_threshold(self):
        classifications = { 'parcel': 0.8999243, 'package': 0.9999243, 'delivery': 0.9999243 }
        self.assertTrue(self.matcher.is_delivery(classifications))
