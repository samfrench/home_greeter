import os
import clarifai.rest as cr

class Classifier():
    MODEL = 'delivery'

    def __init__(self, api=None):
        self.__api = api or self.__api()

    def classify_image(self, photo):
        model           = self.__get_model()
        image           = cr.Image(file_obj=photo)
        classifications = model.predict([image])
        return self.__transform(classifications['outputs'][0]['data']['concepts'])

    def __transform(self, concepts):
        transformed_data = {}
        for concept in concepts:
            transformed_data[concept['name']] = concept['value']
        return transformed_data

    def __get_model(self):
        return self.__api.models.get(self.MODEL)

    def __api(self):
        return cr.ClarifaiApp(api_key=os.getenv('CLARIFAI_API_KEY'))
