import RPi.GPIO as GPIO

class Button():
    INPUT_PIN = 15

    def __init__(self):
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(self.INPUT_PIN, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

    def subscribe(self, callback):
        GPIO.add_event_detect(self.INPUT_PIN, GPIO.RISING, callback=callback, bouncetime=5000)
