from .listener import Listener
from .speaker import Speaker

class Greeter():
    def __init__(self):
        self.listener = Listener('sphinx') # sphinx | google
        self.speaker = Speaker('say') # say | espeak

    def welcome(self):
        self.speaker.speak('Hello. I am the smart home greeter.')

    def ask_for_name(self):
        self.speaker.speak('What is your name?')

        return self.listener.listen()

    def ask_for_person(self):
        self.speaker.speak('Who are you here to see?')

        return self.listener.listen()

    def update_while_finding_if_person_is_avaiable(self, name, person):
        self.speaker.speak("Thank you {name}. Verifying if {person} is available to come to the door.".format(name=name, person=person))
