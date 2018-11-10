from unittest import TestCase
from mock import Mock, call, patch
from home_greeter import Controller

class TestControllerWithVisitorAndOccupierIn(TestCase):
    def setUp(self):
        self.mock_detector = Mock(autospec='home_greeter.Detector')
        self.mock_detector.subscribe = lambda x : x()
        self.mock_greeter = Mock(autospec='home_greeter.Greeter')
        self.mock_camera  = Mock(autospec='home_greeter.Camera')
        self.mock_tweeter = Mock(autospec='home_greeter.Tweeter')
        self.controller = Controller(
            detector=self.mock_detector, greeter=self.mock_greeter, camera=self.mock_camera, tweeter=self.mock_tweeter
        )
        self.controller.should_run(False)

    def test_create(self):
        self.assertIsInstance(self.controller, Controller)

    def test_greeter_welcome_is_called(self):
        self.controller.run()
        self.mock_greeter.welcome.assert_called_once()

    def test_greeter_ask_for_visitor_name_is_called(self):
        self.controller.run()
        self.mock_greeter.ask_for_visitor_name.assert_called_once()

    def test_greeter_ask_for_occupier_name_is_called(self):
        self.controller.run()
        self.mock_greeter.ask_for_occupier_name.assert_called_once()

    def test_greeter_update_visitor_about_asking_for_occupier_is_called(self):
        with patch.object(self.mock_greeter, 'ask_for_visitor_name', return_value='Bob'):
            with patch.object(self.mock_greeter, 'ask_for_occupier_name', return_value='Alice'):
                self.controller.run()
                self.mock_greeter.update_visitor_about_asking_for_occupier.assert_called_once_with('Bob', 'Alice')

    def test_greeter_request_occupier_come_to_the_door_is_called(self):
        self.controller.run()
        self.mock_greeter.request_occupier_come_to_the_door.assert_called_once()

    # Multiple items are returned when waiting for input
    # As long as the first is True this will stop the application flow
    @patch('select.select', return_value=[True, None, None])
    def test_occupier_at_door_so_no_other_methods_called(self, keypress):
        self.controller.run()
        self.mock_greeter.take_message_for_occupier.assert_not_called()
        self.mock_greeter.take_photo.assert_not_called()
        self.mock_camera.take_photo.assert_not_called()
        self.mock_tweeter.tweet_message_with_image.assert_not_called()
        self.mock_greeter.thank_visitor.assert_not_called()

class TestControllerWithVisitorAndOccupierOut(TestCase):
    def setUp(self):
        self.mock_detector = Mock(autospec='home_greeter.Detector')
        self.mock_detector.subscribe = lambda x : x()
        self.mock_greeter = Mock(autospec='home_greeter.Greeter')
        self.mock_camera  = Mock(autospec='home_greeter.Camera')
        self.mock_tweeter = Mock(autospec='home_greeter.Tweeter')
        self.controller = Controller(
            detector=self.mock_detector, greeter=self.mock_greeter, camera=self.mock_camera, tweeter=self.mock_tweeter
        )
        self.controller.should_run(False)

    def test_create(self):
        self.assertIsInstance(self.controller, Controller)

    def test_greeter_welcome_is_called(self):
        self.controller.run()
        self.mock_greeter.welcome.assert_called_once()

    def test_greeter_ask_for_visitor_name_is_called(self):
        self.controller.run()
        self.mock_greeter.ask_for_visitor_name.assert_called_once()

    def test_greeter_ask_for_occupier_name_is_called(self):
        self.controller.run()
        self.mock_greeter.ask_for_occupier_name.assert_called_once()

    def test_greeter_update_visitor_about_asking_for_occupier_is_called(self):
        with patch.object(self.mock_greeter, 'ask_for_visitor_name', return_value='Bob'):
            with patch.object(self.mock_greeter, 'ask_for_occupier_name', return_value='Alice'):
                self.controller.run()
                self.mock_greeter.update_visitor_about_asking_for_occupier.assert_called_once_with('Bob', 'Alice')

    def test_greeter_request_occupier_come_to_the_door_is_called(self):
        self.controller.run()
        self.mock_greeter.request_occupier_come_to_the_door.assert_called_once()

    def test_greeter_take_message_is_called(self):
        self.controller.run()
        self.mock_greeter.take_message_for_occupier.assert_called_once()

    def test_greeter_take_photo_is_called(self):
        self.controller.run()
        self.mock_greeter.take_photo.assert_called_once()

    def test_camera_take_photo_is_called(self):
        self.controller.run()
        self.mock_camera.take_photo.assert_called_once()

    def test_tweeter_tweet_message_with_image_is_called(self):
        with patch.object(self.mock_greeter, 'take_message_for_occupier', return_value='I am outside'):
            with patch.object(self.mock_camera, 'take_photo', return_value='/path/to/image.jpg'):
                self.controller.run()
                self.mock_tweeter.tweet_message_with_image.assert_called_once_with('I am outside', '/path/to/image.jpg')

    def test_greeter_thank_visitor_is_called(self):
        self.controller.run()
        self.mock_greeter.thank_visitor.assert_called_once()
