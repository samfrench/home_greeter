from mock import Mock, patch

class MockPi():
    MockRPi = Mock()
    modules = {
        'RPi': MockRPi,
        'RPi.GPIO': MockRPi.GPIO,
        'picamera': MockRPi
    }

    patcher = patch.dict('sys.modules', modules)
    patcher.start()
