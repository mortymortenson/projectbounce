from enum import Enum
import datetime
import logging
import os
import sys

time = datetime.datetime

class Action(Enum):
    Buy = 1
    Sell = 2

class Side(Enum):
    Bid = 1
    Ask = 2

class Right(Enum):
    Put = "P"
    Call = "C"

class TradeRequest(object):
    def __init__(self,
            contract,
            action: Action,
            price: float,
            size: float):
        self.contract = contract
        self.action = action
        self.price = price
        self.size = size

class BError(RuntimeError):
    pass

def setupLogger(base: str=None) -> None:

    recfmt = '(%(threadName)s) %(asctime)s.%(msecs)03d %(levelname)s %(filename)s:%(lineno)d %(message)s'
    timefmt = '%y%m%d %H:%M:%S'

    if base:
        if not os.path.exists("log"):
            os.makedirs("log")
        now = time.now().strftime("%Y%m%d.%H%M%S")
        filename = os.path.join("log", f"{base}.{now}.log")
    else:
        filename = None

    logging.basicConfig(filename=filename,
                        filemode="w",
                        level=logging.DEBUG,
                        format=recfmt, datefmt=timefmt)

    if filename:
        logger = logging.getLogger()
        console = logging.StreamHandler()
        console.setLevel(logging.DEBUG)
        console.setFormatter(logging.Formatter(recfmt))
        logger.addHandler(console)

