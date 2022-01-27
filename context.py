import datetime

# This module is our application context; e.g. if we ever want to do historical
# simulation, we can use this for state like current sim time, etc.

COMMAND = None
def init():
    global COMMAND
    if COMMAND:
        raise Exception("Cannot call init more than once")
    COMMAND = True

def now():
    if not COMMAND:
        raise Exception("Not initialized")
    return datetime.datetime.now()
