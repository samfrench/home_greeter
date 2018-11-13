from unittest import TestCase
from mock import patch
import RPi.GPIO as GPIO
import gpio_helper

from home_greeter.detector.sensor import Sensor

class TestSensor(TestCase):
    def setUp(self):
        gpio_helper.reset_pins()

    def test_create(self):
        sensor = Sensor()
        self.assertIsInstance(sensor, Sensor)

    @patch('RPi.GPIO.setmode')
    def test_create_mode_called(self, mock_gpio_mode):
        sensor = Sensor()
        mock_gpio_mode.assert_called_once_with(GPIO.BCM)

    @patch('RPi.GPIO.setup')
    def test_create_setup_called(self, mock_gpio_setup):
        sensor = Sensor()
        mock_gpio_setup.assert_called_once_with(sensor.INPUT_PIN, GPIO.IN)

    @patch('RPi.GPIO.add_event_detect')
    def test_subscribe(self, mock_gpio_add_event_detect):
        callback = lambda _ : 'called!'
        sensor = Sensor()
        sensor.subscribe(callback)
        mock_gpio_add_event_detect.assert_called_once_with(
            sensor.INPUT_PIN, GPIO.RISING, callback=callback, bouncetime=200
        )

    @classmethod
    def tearDownClass(self):
        gpio_helper.close()
