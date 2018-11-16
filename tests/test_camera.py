from unittest import TestCase
from mock import Mock, call, patch

# Mocking picamera module before camera import
import sys
sys.modules['picamera'] = Mock()

from home_greeter.camera import Camera

class TestCamera(TestCase):
    def setUp(self):
        self.camera = Camera()

    def test_create(self):
        self.assertIsInstance(self.camera, Camera)

    def test_take_photo(self):
        location = '/path/to/image.jpg'
        self.camera.take_photo(location)
        self.camera._Camera__camera.capture.assert_called_once_with(location)
