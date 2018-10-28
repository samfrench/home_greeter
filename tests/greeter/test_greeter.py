from unittest import TestCase
from home_greeter import Greeter

class TestGreeter(TestCase):
    def test_create(self):
        self.greeter = Greeter()
        self.assertIsInstance(self.greeter, Greeter)
