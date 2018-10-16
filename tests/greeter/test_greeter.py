from unittest import TestCase
from home_greeter.greeter.greeter import Greeter

class GreeterTest(TestCase):
    def test_create(self):
        self.greeter = Greeter()
        self.assertIsInstance(self.greeter, Greeter)
