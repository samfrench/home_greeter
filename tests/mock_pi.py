from mock import MagicMock, patch

class MockPi():
    MockRPi = MagicMock()
    modules = {
        'RPi': MockRPi,
        'RPi.GPIO': MockRPi.GPIO,
    }

    patcher = patch.dict('sys.modules', modules)
    patcher.start()
