from unittest import TestCase
from mock import patch, MagicMock, call
from home_greeter import Controller

class TestController(TestCase):
    def setUp(self):
        self.mock_greeter = MagicMock(autospec='home_greeter.Greeter')
        self.controller = Controller(self.mock_greeter)

    def test_create(self):
        self.assertIsInstance(self.controller, Controller)

    def test_greeter_welcome_is_called(self):
        self.controller.process()
        self.mock_greeter.assert_has_calls([call.welcome()])

    def test_greeter_ask_for_name_is_called(self):
        self.controller.process()
        self.mock_greeter.assert_has_calls([call.ask_for_name()])

    def test_greeter_ask_for_person_is_called(self):
        self.controller.process()
        self.mock_greeter.assert_has_calls([call.ask_for_person()])