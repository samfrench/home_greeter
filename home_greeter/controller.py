from os import environ
import sys, select
from home_greeter.detector import Detector
from home_greeter.greeter.greeter import Greeter
from home_greeter.camera import Camera
from home_greeter.tweeter import Tweeter

class Controller():
    def __init__(self, detector=Detector(), greeter=Greeter(), camera=Camera(), tweeter=Tweeter()):
        self.__detector   = detector
        self.__greeter    = greeter
        self.__camera     = camera
        self.__tweeter    = tweeter
        self.__should_run = False if ('NOHALT' in environ and environ['NOHALT'].lower() in ['false']) else True

    def should_run(self, should_run=True):
        self.__should_run = should_run

    def run(self):
        self.__detector.subscribe(self.__process)
        while self.__should_run:
            pass

    def __process(self):
        self.__greeter.welcome()

        # @todo: Detect and handle delivery
        delivery = False
        if (delivery):
            self.__handle_delivery()
        else:
            self.__handle_visitor()

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
        photo = self.__camera.take_photo()

        self.__tweeter.tweet_message_with_image(message, photo)

        self.__greeter.thank_visitor(visitor_name, occupier_name)

    def __handle_delivery(self):
        pass

    def __occupier_at_door(self):
        timeout = 30 if self.__should_run else 0
        i, o, e = select.select([sys.stdin], [], [], timeout)
        if (i):
            # Occupier at door
            return True
        else:
            # Occupier not at door
            return False
