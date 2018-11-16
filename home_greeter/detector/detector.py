from .button import Button
from .sensor import Sensor

class Detector():
    def __init__(self, button=None, sensor=None):
        self.button = button or Button()
        self.sensor = sensor or Sensor()

    def subscribe(self, callback):
        self.button.subscribe(callback)
        self.sensor.subscribe(callback)
