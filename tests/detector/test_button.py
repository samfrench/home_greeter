from unittest import TestCase
from mock import patch
import RPi.GPIO as GPIO
from home_greeter.detector.button import Button

class TestButton(TestCase):
    def test_create(self):
        button = Button()
        self.assertIsInstance(button, Button)

    @patch('RPi.GPIO.setmode')
    def test_create_mode_called(self, mock_gpio_mode):
        button = Button()
        mock_gpio_mode.assert_called_once_with(GPIO.BCM)

    @patch('RPi.GPIO.setup')
    def test_create_setup_called(self, mock_gpio_setup):
        button = Button()
        mock_gpio_setup.assert_called_once_with(button.INPUT_PIN, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

    @patch('RPi.GPIO.add_event_detect')
    def test_subscribe(self, mock_gpio_add_event_detect):
        callback = lambda _ : 'called!'
        button = Button()
        button.subscribe(callback)
        mock_gpio_add_event_detect.assert_called_once_with(
            button.INPUT_PIN, GPIO.RISING, callback=callback, bouncetime=200
        )
