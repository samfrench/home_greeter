from mock import Mock, patch

class MockPi():
    MockRPi = Mock()
    modules = {
        'RPi': MockRPi,
        'RPi.GPIO': MockRPi.GPIO,
    }

    patcher = patch.dict('sys.modules', modules)
    patcher.start()
