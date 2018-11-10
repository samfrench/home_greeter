from unittest import TestCase
from mock import Mock, call, MagicMock, patch
import speech_recognition as sr
from home_greeter.greeter.listener import Listener

class TestListenerWithSphinx(TestCase):
    def setUp(self):
        self.mock_recogniser = Mock(autospec='sr.Recognizer')
        self.mock_microphone = MagicMock(autospec='sr.Microphone')
        self.listener = Listener(service='sphinx', recogniser=self.mock_recogniser, microphone=self.mock_microphone)

    def test_create(self):
        self.assertIsInstance(self.listener, Listener)

    def test_listen(self):
        self.listener.listen()

        # __enter__ is needed due to logic in listener class being inside a python 'with' block
        # when you use 'with', this calls a magic method of __enter__ passing result to 'as'
        self.mock_recogniser.assert_has_calls([
            call.adjust_for_ambient_noise(self.mock_microphone.__enter__()),
            call.listen(self.mock_microphone.__enter__())
        ])

    def test_listen_raises_value_error(self):
        with patch.object(self.listener, 'transcribe') as transcribe:
            transcribe.side_effect = sr.UnknownValueError()

            with self.assertRaises(ValueError) as context:
                self.listener.listen()

            self.assertIn('Could not translate speech', str(context.exception))

    def test_transcribe(self):
        audio = lambda: None
        self.listener.transcribe(audio)

        self.mock_recogniser.assert_has_calls([call.recognize_sphinx(audio)])

class TestListenerWithGoogle(TestCase):
    def setUp(self):
        self.mock_recogniser = Mock(autospec='sr.Recognizer')
        self.mock_microphone = MagicMock(autospec='sr.Microphone')
        self.listener = Listener(service='google', recogniser=self.mock_recogniser, microphone=self.mock_microphone)

    def test_create(self):
        self.assertIsInstance(self.listener, Listener)

    def test_listen(self):
        self.listener.listen()

        # __enter__ is needed due to logic in listener class being inside a python 'with' block
        # when you use 'with', this calls a magic method of __enter__ passing result to 'as'
        self.mock_recogniser.assert_has_calls([
            call.adjust_for_ambient_noise(self.mock_microphone.__enter__()),
            call.listen(self.mock_microphone.__enter__())
        ])

    def test_listen_raises_connection_error(self):
        with patch.object(self.listener, 'transcribe') as transcribe:
            transcribe.side_effect = sr.RequestError()

            with self.assertRaises(Exception) as context:
                self.listener.listen()

            self.assertIn('Error connecting to API', str(context.exception))

    def test_listen_raises_value_error(self):
        with patch.object(self.listener, 'transcribe') as transcribe:
            transcribe.side_effect = sr.UnknownValueError()

            with self.assertRaises(ValueError) as context:
                self.listener.listen()

            self.assertIn('Could not translate speech', str(context.exception))

    def test_transcribe(self):
        audio = lambda: None
        self.listener.transcribe(audio)

        self.mock_recogniser.assert_has_calls([call.recognize_google(audio)])

class TestListenerWithInvalidService(TestCase):
    def setUp(self):
        self.mock_recogniser = Mock(autospec='sr.Recognizer')
        self.mock_microphone = MagicMock(autospec='sr.Microphone')

    def test_create(self):
        with self.assertRaises(NotImplementedError) as context:
            Listener(service='invalid-service', recogniser=self.mock_recogniser, microphone=self.mock_microphone)

        self.assertIn('No available speech to text recognition service chosen.', str(context.exception))

class TestListenerWithNoService(TestCase):
    def setUp(self):
        self.mock_recogniser = Mock(autospec='sr.Recognizer')
        self.mock_microphone = MagicMock(autospec='sr.Microphone')

    def test_create(self):
        with self.assertRaises(NotImplementedError) as context:
            Listener(recogniser=self.mock_recogniser, microphone=self.mock_microphone)

        self.assertIn('No available speech to text recognition service chosen.', str(context.exception))
