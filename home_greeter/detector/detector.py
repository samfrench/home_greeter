from .button import Button
from .sensor import Sensor

class Detector():
    def __init__(self, button = Button(), sensor = Sensor()):
        self.button = button
        self.sensor = sensor

    def subscribe(self, callback):
        self.button.subscribe(callback)
        self.sensor.subscribe(callback)
