from unittest import TestCase
from mock import call, patch
from home_greeter.greeter.speaker import Speaker

class TestSpeakerWithSay(TestCase):
    def setUp(self):
        self.speaker = Speaker(service='say')

    def test_create(self):
        self.assertIsInstance(self.speaker, Speaker)

    @patch('os.system')
    def test_speak(self, mock_os):
        text = 'Text for testing with say'
        self.speaker.speak(text)
        mock_os.assert_has_calls([call("say '{text}'".format(text=text))])

class TestSpeakerWithEspeak(TestCase):
    def setUp(self):
        self.speaker = Speaker(service='espeak')

    def test_create(self):
        self.assertIsInstance(self.speaker, Speaker)

    @patch('os.system')
    def test_speak(self, mock_os):
        text = 'Text for testing with espeak'
        self.speaker.speak(text)
        mock_os.assert_has_calls([call("espeak '{text}'".format(text=text))])

class TestSpeakerWithInvalidService(TestCase):
    def test_create(self):
        with self.assertRaises(NotImplementedError) as context:
            Speaker(service='invalid-service')

        self.assertIn('No available text to speech service chosen.', str(context.exception))

class TestSpeakerWithNoService(TestCase):
    def test_create(self):
        with self.assertRaises(NotImplementedError) as context:
            Speaker()

        self.assertIn('No available text to speech service chosen.', str(context.exception))
