from unittest import TestCase
from mock import patch
from tests.mock_pi import MockPi
import RPi.GPIO

from home_greeter.detector.button import Button

class TestButton(TestCase):
    def setUp(self):
        self.button = Button()

    def test_create(self):
        self.assertIsInstance(self.button, Button)

    @patch('RPi.GPIO.setmode')
    def test_create_mode_called(self, mock_gpio_mode):
        self.button = Button()
        mock_gpio_mode.assert_called_once_with(RPi.GPIO.BCM)

    @patch('RPi.GPIO.setup')
    def test_create_setup_called(self, mock_gpio_setup):
        self.button = Button()
        mock_gpio_setup.assert_called_once_with(self.button.INPUT_PIN, RPi.GPIO.IN)

    @patch('RPi.GPIO.add_event_detect')
    def test_subscribe(self, mock_gpio_add_event_detect):
        callback = lambda _ : 'called!'
        self.button.subscribe(callback)
        mock_gpio_add_event_detect.assert_called_once_with(self.button.INPUT_PIN, RPi.GPIO.RISING, callback=callback)
