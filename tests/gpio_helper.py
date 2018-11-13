import RPi.GPIO as GPIO

def reset_pins():
    GPIO.__pins_dict = dict()

def get_mode():
    print(dir(GPIO))
    return GPIO.__setmode

def close():
    import threading
    for t in threading.enumerate():
        if t != threading.main_thread():
            if t._tstate_lock.locked():
                t._tstate_lock.release()

def pins():
    return GPIO.__pins_dict
