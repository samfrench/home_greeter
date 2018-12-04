from unittest import TestCase
from mock import Mock, call
from home_greeter.greeter import Greeter

class TestGreeter(TestCase):
    def setUp(self):
        self.mock_listener = Mock(autospec='home_greeter.greeter.Listener')
        self.mock_speaker = Mock(autospec='home_greeter.greeter.Speaker')
        self.greeter = Greeter(listener=self.mock_listener, speaker=self.mock_speaker)

    def test_create(self):
        self.assertIsInstance(self.greeter, Greeter)

    def test_welcome(self):
        self.greeter.welcome()
        self.mock_speaker.speak.assert_called_once_with('Hello. I am the smart home greeter.')

    def test_ask_for_visitor_name(self):
        self.greeter.ask_for_visitor_name()
        self.mock_speaker.speak.assert_called_once_with('What is your name?')
        self.mock_listener.listen.assert_called_once()

    def test_ask_for_occupier_name(self):
        self.greeter.ask_for_occupier_name()
        self.mock_speaker.speak.assert_called_once_with('Who are you here to see?')
        self.mock_listener.listen.assert_called_once()

    def test_update_visitor_about_asking_for_occupier(self):
        self.greeter.update_visitor_about_asking_for_occupier('Bob', 'Alice')
        self.mock_speaker.speak.assert_called_once_with(
            'Thank you Bob. Verifying if Alice is available to come to the door.'
        )

    def test_request_occupier_come_to_the_door(self):
        self.greeter.request_occupier_come_to_the_door('Bob', 'Alice')
        self.mock_speaker.speak.assert_called_once_with(
            'Bob is outside requesting to visit Alice.'
        )

    def test_take_message_for_occupier(self):
        self.greeter.take_message_for_occupier('Alice')
        self.mock_speaker.speak.assert_called_once_with(
            'Alice is unable to come to the door. Please leave a short message for them.'
        )
        self.mock_listener.listen.assert_called_once()

    def test_take_photo(self):
        self.greeter.take_photo()
        self.mock_speaker.speak.assert_called_once_with('A photo is being taken.')

    def test_thank_visitor(self):
        self.greeter.thank_visitor('Bob', 'Alice')
        self.mock_speaker.speak.assert_called_once_with(
            'Thank you Bob. The message and photo will be passed on to Alice.'
        )

    def test_ask_deliverer_to_wait(self):
        self.greeter.ask_deliverer_to_wait()
        self.mock_speaker.speak.assert_called_once_with(
            'Please wait. Checking if someone is available to come to the door.'
        )

    def test_request_someone_come_to_the_door(self):
        self.greeter.request_someone_come_to_the_door()
        self.mock_speaker.speak.assert_called_once_with('Answer the door. There is a delivery.')

    def test_ask_deliverer_to_leave_parcel(self):
        self.greeter.ask_deliverer_to_leave_parcel()
        self.mock_speaker.speak.assert_called_once_with(
            'There is no one available at the moment. Please leave the delivery next door.'
        )
