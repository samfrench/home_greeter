from mock import Mock, patch

class MockPi():
    MockRPi = Mock()
    modules = {
        'picamera': Mock()
    }

    patcher = patch.dict('sys.modules', modules)
    patcher.start()
