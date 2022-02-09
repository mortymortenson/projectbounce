import datetime
import util

# This module is our application context; e.g. if we ever want to do historical
# simulation, we can use this for state like current sim time, etc.

COMMAND = None
def init() -> None:
    global COMMAND
    if COMMAND:
        raise util.BError("Cannot call init more than once")
    COMMAND = True

def now() -> util.time:
    if not COMMAND:
        raise util.BError("Not initialized")
    return datetime.datetime.now()
