import RPi.GPIO as GPIO

class Sensor():
    INPUT_PIN = 18

    def __init__(self):
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(self.INPUT_PIN, GPIO.IN)

    def subscribe(self, callback):
        GPIO.add_event_detect(self.INPUT_PIN, GPIO.RISING, callback=callback, bouncetime=200)
