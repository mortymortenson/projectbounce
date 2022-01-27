from enum import Enum
from util import Right, Action, Side
from ibapi.contract import *
import datetime
import ib
import autolist

TS_FMT = "%Y-%m-%d %H:%M:%S"

lastSymbolId = 0
def _nextSID():
    global lastSymbolId
    lastSymbolId += 1
    return lastSymbolId

def getSIDList(default=None):
    return autolist.AutoList(lastSymbolId + 1, default=default)

class BounceEquity(Contract):
    def __init__(self, symbol, exchange="SMART"):
        Contract.__init__(self)
        self.symbol = symbol
        self.secType = "STK"
        self.currency = "USD"
        self.exchange = exchange

        self.sid = _nextSID()

    def __str__(self):
        return self.symbol

class BounceOption(Contract):
    def __init__(self, equitySymbol, putCall, expirationDate, strikePrice):
        Contract.__init__(self)
        self.symbol = equitySymbol
        self.secType = "OPT"
        self.currency = "USD"
        self.exchange = "ISE" # TODO
        self.lastTradeDateOrContractMonth = expirationDate
        self.right = putCall
        self.strike = strikePrice
        self.multiplier = "100"

        self.sid = _nextSID()

    def __str__(self):
        return "[%s %s %s %s]" % (
                self.symbol,
                self.lastTradeDateOrContractMonth,
                self.right,
                self.strike)
