from unittest import TestCase
from mock import Mock, call
from home_greeter import Greeter

class TestGreeter(TestCase):
    def setUp(self):
        self.mock_listener = Mock(autospec='home_greeter.greeter.Listener')
        self.mock_speaker = Mock(autospec='home_greeter.greeter.Speaker')
        self.greeter = Greeter(listener=self.mock_listener, speaker=self.mock_speaker)

    def test_create(self):
        self.greeter = Greeter()
        self.assertIsInstance(self.greeter, Greeter)

    def test_welcome(self):
        self.greeter.welcome()
        self.mock_speaker.assert_has_calls([call.speak('Hello. I am the smart home greeter.')])

    def test_ask_for_name(self):
        self.greeter.ask_for_name()
        self.mock_speaker.assert_has_calls([call.speak('What is your name?')])
        self.mock_listener.assert_has_calls([call.listen()])

    def test_ask_for_person(self):
        self.greeter.ask_for_person()
        self.mock_speaker.assert_has_calls([call.speak('Who are you here to see?')])
        self.mock_listener.assert_has_calls([call.listen()])

    def test_update_while_finding_if_person_is_avaiable(self):
        self.greeter.update_while_finding_if_person_is_avaiable('Bob', 'Alice')
        self.mock_speaker.assert_has_calls([
            call.speak('Thank you Bob. Verifying if Alice is available to come to the door.')
        ])
