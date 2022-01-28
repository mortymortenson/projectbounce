from enum import Enum
from util import Right, Action, Side
from ibapi.contract import *
import datetime
import ib
import autolist
import typing

TS_FMT = "%Y-%m-%d %H:%M:%S"

lastSymbolId = 0
def _nextSID() -> int:
    global lastSymbolId
    lastSymbolId += 1
    return lastSymbolId

Type = typing.TypeVar("Type")
def getSIDList(default: typing.Callable[[], Type]=None) -> autolist.AutoList[Type]:
    return autolist.AutoList(lastSymbolId + 1, default=default)

class BounceSymbol(object):
    def __init__(self):
        self.sid = _nextSID()

class BounceEquity(BounceSymbol, Contract):
    def __init__(self, symbol: str, exchange: str="SMART"):
        BounceSymbol.__init__(self)
        Contract.__init__(self)
        self.symbol = symbol
        self.secType = "STK"
        self.currency = "USD"
        self.exchange = exchange

    def __str__(self) -> str:
        return self.symbol

class BounceOption(BounceSymbol, Contract):
    def __init__(self, equitySymbol: str, putCall: Right, expirationDate: str, strikePrice: float):
        BounceSymbol.__init__(self)
        Contract.__init__(self)
        self.symbol = equitySymbol
        self.secType = "OPT"
        self.currency = "USD"
        self.exchange = "ISE" # TODO
        self.lastTradeDateOrContractMonth = expirationDate
        self.right = putCall
        self.strike = strikePrice
        self.multiplier = "100"

    def __str__(self) -> str:
        return "[%s %s %s %s]" % (
                self.symbol,
                self.lastTradeDateOrContractMonth,
                self.right,
                self.strike)
