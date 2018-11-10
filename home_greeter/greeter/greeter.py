from .listener import Listener
from .speaker import Speaker

class Greeter():
    def __init__(self, listener=None, speaker=None):
        self.__listener = listener or Listener(service='sphinx') # sphinx | google
        self.__speaker = speaker or Speaker(service='say') # say | espeak

    def welcome(self):
        self.__speaker.speak('Hello. I am the smart home greeter.')

    def ask_for_name(self):
        self.__speaker.speak('What is your name?')

        return self.__listener.listen()

    def ask_for_person(self):
        self.__speaker.speak('Who are you here to see?')

        return self.__listener.listen()

    def update_while_finding_if_person_is_avaiable(self, name, person):
        self.__speaker.speak("Thank you {name}. Verifying if {person} is available to come to the door.".format(name=name, person=person))
