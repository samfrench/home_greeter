from picamera import PiCamera

class Camera():
    def __init__(self):
        self.__camera = PiCamera()

    def take_photo(self):
        self.__camera.capture('/home/pi/Desktop/image.jpg')
