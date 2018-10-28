from home_greeter.detector import Detector
from home_greeter.greeter.greeter import Greeter
from home_greeter.tweeter import Tweeter

class Controller():
    def __init__(self, detector=Detector(), greeter=Greeter(), tweeter=Tweeter(), should_run=True):
        self.__detector = detector
        self.__greeter = greeter
        self.__tweeter = tweeter
        self.__should_run = should_run

    def run(self):
        self.__detector.subscribe(self.process)
        while self.__should_run:
            pass

    def process(self):
        self.__greeter.welcome()

        self.__name = self.__greeter.ask_for_name()
        print(self.__name)

        # detect delivery or not

        self.__person = self.__greeter.ask_for_person()
        print(self.__person)

        # check if person is available

        # if not available then take and tweet image

        self.__tweeter.tweet_image()
