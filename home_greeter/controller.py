import os
import sys, select
from time import sleep
import RPi.GPIO as GPIO
from home_greeter.detector.detector import Detector
from home_greeter.greeter.greeter import Greeter
from home_greeter.camera import Camera
from home_greeter.imager.imager import Imager
from home_greeter.tweeter import Tweeter

class Controller():
    INITIAL_PHOTO = os.getenv('INITIAL_PHOTO')
    VISITOR_PHOTO = os.getenv('VISITOR_PHOTO')

    def __init__(self, detector=None, greeter=None, camera=None, imager=None, tweeter=None):
        self.__detector    = detector or Detector()
        self.__greeter     = greeter  or Greeter()
        self.__camera      = camera   or Camera()
        self.__imager      = imager   or Imager()
        self.__tweeter     = tweeter  or Tweeter()
        self.__should_run  = False if ('NOHALT' in os.environ and os.environ['NOHALT'].lower() in ['false']) else True
        self.__has_visitor = False

    def should_run(self, should_run=True):
        self.__should_run = should_run

    def run(self):
        try:
            self.__detector.subscribe(self.__process)
            while self.__should_run:
                sleep(1)
                pass
        except KeyboardInterrupt:
            pass
        finally:
            GPIO.cleanup()

    def __process(self, channel):
        if self.__has_visitor:
            return

        self.__has_visitor = True

        self.__greeter.welcome()

        if (self.__is_delivery()):
            self.__handle_delivery()
        else:
            self.__handle_visitor()

        self.__has_visitor = False

    def __is_delivery(self):
        self.__camera.take_photo(self.INITIAL_PHOTO)
        return self.__imager.is_delivery(self.INITIAL_PHOTO)

    def __handle_visitor(self):
        visitor_name = self.__greeter.ask_for_visitor_name()

        occupier_name = self.__greeter.ask_for_occupier_name()

        # Update the visitor at the door
        self.__greeter.update_visitor_about_asking_for_occupier(visitor_name, occupier_name)

        # Ask for occupier to come to the door
        # For simplicity this uses the same speaker but can use a display
        # Or even send a message to the occupier's phone
        # I thought avoiding sending a message for this part due to that happening when they are unavailable
        self.__greeter.request_occupier_come_to_the_door(visitor_name, occupier_name)

        # I thought about adding a sensor or to detect a door opening, but there is already a movement sensor
        # for initialising the scenario
        # For simplicity I wait a set time for the occupier to come to the door

        if self.__occupier_at_door():
            return

        # Occupier not able to be at door so continuing main flow

        message = self.__greeter.take_message_for_occupier(occupier_name)

        self.__greeter.take_photo()
        self.__camera.take_photo(self.VISITOR_PHOTO)

        self.__tweeter.tweet_message_with_image(message, self.VISITOR_PHOTO)

        self.__greeter.thank_visitor(visitor_name, occupier_name)

    def __handle_delivery(self):
        self.__greeter.ask_deliverer_to_wait()

        self.__greeter.request_someone_come_to_the_door()

        # I thought about adding a sensor or to detect a door opening, but there is already a movement sensor
        # for initialising the scenario
        # For simplicity I wait a set time for the occupier to come to the door

        if self.__occupier_at_door():
            return

        self.__greeter.ask_deliverer_to_leave_parcel()

    def __occupier_at_door(self):
        timeout = 30 if self.__should_run else 0
        i, o, e = select.select([sys.stdin], [], [], timeout)
        if (i):
            # Occupier at door
            return True
        else:
            # Occupier not at door
            return False
