from .listener import Listener
from .speaker import Speaker

class Greeter():
    def __init__(self, listener=None, speaker=None):
        self.__listener = listener or Listener(service='sphinx') # sphinx | google
        self.__speaker = speaker or Speaker(service='say') # say | espeak

    def welcome(self):
        self.__speaker.speak('Hello. I am the smart home greeter.')

    def ask_for_visitor_name(self):
        self.__speaker.speak('What is your name?')

        return self.__listener.listen()

    def ask_for_occupier_name(self):
        self.__speaker.speak('Who are you here to see?')

        return self.__listener.listen()

    def update_visitor_about_asking_for_occupier(self, visitor_name, occupier_name):
        self.__speaker.speak(
            "Thank you {visitor_name}. Verifying if {occupier_name} is available to come to the door."
                .format(visitor_name=visitor_name, occupier_name=occupier_name)
        )

    def request_occupier_come_to_the_door(self, visitor_name, occupier_name):
        self.__speaker.speak(
            "{visitor_name} is outside requesting to visit {occupier_name}."
                .format(visitor_name=visitor_name, occupier_name=occupier_name)
        )

    def take_message_for_occupier(self, occupier_name):
        self.__speaker.speak(
            "{occupier_name} is unable to come to the door. Please leave a short message for them."
            .format(occupier_name=occupier_name)
        )

        return self.__listener.listen()

    def take_photo(self):
        self.__speaker.speak('A photo is being taken.')

    def thank_visitor(self):
        self.__speaker.speak('The message and photo will be passed on.')

    def ask_deliverer_to_wait(self):
        self.__speaker.speak('Please wait. Checking if someone is available to come to the door.')

    def request_someone_come_to_the_door(self):
        self.__speaker.speak('Answer the door. There is a delivery.')

    def ask_deliverer_to_leave_parcel(self):
        self.__speaker.speak('There is no one available at the moment. Please leave the delivery next door.')
