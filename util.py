from enum import Enum, IntEnum
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

LogBlack        = '0;30'
LogRed          = '0;31'
LogGreen        = '0;32'
LogBrownOrange  = '0;33'
LogBlue         = '0;34'
LogPurple       = '0;35'
LogCyan         = '0;36'
LogLightGray    = '0;37'
LogDarkGray     = '1;30'
LogLightRed     = '1;31'
LogLightGreen   = '1;32'
LogYellow       = '1;33'
LogLightBlue    = '1;34'
LogLightPurple  = '1;35'
LogLightCyan    = '1;36'
LogWhite        = '1;37'

LOG_RESET_SEQ = r"\033[0m"
LOG_COLOR_SEQ = r"\033[1;%dm"
LOG_BOLD_SEQ = r"\033[1m"

def logColor(s: str, color: str) -> str:
    s = "\033[" + color + "m" + s + "\033[0m"
    return s

class Level:
    def __init__(self):
        self.price = 0
        self.size = 0
        self.count = 0

class Book:
    def __init__(self, symbol):
        self.symbol = symbol
        self.bid = Level()
        self.ask = Level()


