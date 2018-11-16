from .classifier import Classifier
from .matcher import Matcher

class Imager():
    def __init__(self, classifier=None, matcher=None):
        self.__classifier = classifier or Classifier()
        self.__matcher    = matcher    or Matcher()

    def is_delivery(self, photo):
        classifications = self.__classifier.classify_image(photo)
        return self.__matcher.is_delivery(classifications)
