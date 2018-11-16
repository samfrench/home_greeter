import speech_recognition as sr

class Listener:
    def __init__(self, service=None, recogniser=sr.Recognizer(), microphone=sr.Microphone()):
        if service not in ['google', 'sphinx']:
            raise NotImplementedError('No available speech to text recognition service chosen.')

        self.__service    = service
        self.__recogniser = recogniser
        self.__microphone = microphone

    def listen(self):
        with self.__microphone as source:
            # Only keeping below line to show what would be needed if outside
            # self.__recogniser.adjust_for_ambient_noise(source)
            audio = self.__recogniser.listen(source)

        try:
            return self.transcribe(audio)
        except sr.RequestError:
            raise Exception('Error connecting to API')
        except sr.UnknownValueError:
            raise ValueError('Could not translate speech')

    def transcribe(self, audio):
        if self.__service == 'google':
            return self.__recogniser.recognize_google(audio)
        elif self.__service == 'sphinx':
            return self.__recogniser.recognize_sphinx(audio)
