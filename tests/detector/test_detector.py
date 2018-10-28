from unittest import TestCase
from mock import Mock
from tests.mock_pi import MockPi
import RPi.GPIO
from home_greeter import Detector

class TestController(TestCase):
    def setUp(self):
        self.mock_button = Mock(autospec='home_greeter.detector.Button')
        self.mock_sensor = Mock(autospec='home_greeter.detector.Sensor')
        self.detector = Detector(button=self.mock_button, sensor=self.mock_sensor)

    def test_create(self):
        self.assertIsInstance(self.detector, Detector)
