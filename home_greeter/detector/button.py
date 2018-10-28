import RPi.GPIO as GPIO

class Button():
    INPUT_PIN = 25

    def __init__(self):
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(self.INPUT_PIN, GPIO.IN)

    def subscribe(self, callback):
        GPIO.add_event_detect(self.INPUT_PIN, GPIO.RISING, callback=callback)
