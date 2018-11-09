from mock import Mock, patch

class MockTweepy():
    MockTweepy = Mock()
    modules = {
        'tweepy': MockTweepy,
    }

    patcher = patch.dict('sys.modules', modules)
    patcher.start()
