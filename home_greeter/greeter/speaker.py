import os

class Speaker():
    def __init__(self, service):
        self.service = service

    def speak(self, text):
        os.system("{service} '{text}'".format(service=self.service, text=text))
