import speech_recognition as sr

class Listener:

    def __init__(self, service):
        self.service = service
        self.recognizer = sr.Recognizer()
        self.microphone = sr.Microphone()

    def listen(self):
        with self.microphone as source:
            self.recognizer.adjust_for_ambient_noise(source)
            audio = self.recognizer.listen(source)

        try:
            return self.transcribe(audio)
        except sr.RequestError:
            raise Exception('Error connecting to API')
        except sr.UnknownValueError:
            raise ValueError('Could not translate speech')

    def transcribe(self, audio):
        if self.service == 'google':
            return self.recognizer.recognize_google(audio)
        elif self.service == 'sphinx':
            return self.recognizer.recognize_sphinx(audio)
        else:
            raise NotImplementedError('No available speech to text recognition service chosen.')
