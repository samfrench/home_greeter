from unittest import TestCase
from mock import Mock, call, patch
from home_greeter.imager.classifier import Classifier

class TestClassifier(TestCase):
    def setUp(self):
        self.mock_clarifai = Mock(autospec='ClarifaiApp')
        self.classifier    = Classifier(api=self.mock_clarifai)

    def test_create(self):
        self.assertIsInstance(self.classifier, Classifier)

    @patch('clarifai.rest.Image')
    def test_classify_image(self, mock_image):
        models_mock = Mock(autospec='ClarifaiApp.models')
        models_mock.get().predict.return_value = {
            'outputs': [
                {
                    'data': {
                        'concepts': [
                            {
                                'name': 'parcel',
                                'value': 0.9999243
                            },
                            {
                                'name': 'package',
                                'value': 0.9999243
                            },
                            {
                                'name': 'delivery',
                                'value': 0.9999243
                            }
                        ]
                    }
                }
            ]
        }

        self.mock_clarifai.configure_mock(models=models_mock)
        self.classifier = Classifier(api=self.mock_clarifai)

        with open(__file__, 'rb') as photo:
            classifications = self.classifier.classify_image(photo)

            mock_image.assert_called_once_with(file_obj=photo)

        self.mock_clarifai.assert_has_calls([
            call.models.get(Classifier.MODEL),
            call.models.get().predict([mock_image()])
        ])

        self.assertEqual(
            { 'delivery': 0.9999243, 'parcel': 0.9999243, 'package': 0.9999243 },
            classifications
        )
