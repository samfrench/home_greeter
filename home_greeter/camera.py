import os
if os.uname()[1] == 'raspberrypi':
    from picamera import PiCamera
else:
    from mock import Mock
    PiCamera = Mock()

class Camera():
    def __init__(self):
        self.__camera = PiCamera()

    def take_photo(self, file_location):
        self.__camera.capture(file_location)
