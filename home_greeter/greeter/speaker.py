import os

class Speaker():
    def __init__(self, service=None):
        if service not in ['espeak', 'say']:
            raise NotImplementedError('No available text to speech service chosen.')

        self.service = service

    def speak(self, text):
        os.system("{service} '{text}'".format(service=self.service, text=text))
