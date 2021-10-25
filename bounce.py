from enum import Enum
from ibapi.contract import *

class Action(Enum):
    Buy = 1
    Sell = 2

class SupportType(Enum):
    Low = 1
    High = 2

class BounceOption:
    def __init__(self, equity_symbol, put_call, expiration_date, strike_price):
        contract = Contract()
        contract.symbol = equity_symbol
        contract.secType = "OPT"
        contract.currency = "USD"
        contract.exchange = "ISE" # TODO
        contract.lastTradeDateOrContractMonth = expiration_date
        contract.right = put_call
        contract.strike = strike_price
        contract.multiplier = "100"
        self.contract = contract
        self.__repr__ = self.__str__

    def __str__(self):
        return "[%s %s %s %s]" % (
                self.contract.symbol,
                self.contract.lastTradeDateOrContractMonth,
                self.contract.right,
                self.contract.strike)

class BounceTrade:
    def __init__(
            self,
            signal_symbol,
            threshold_price,
            support_type,
            trade_symbol,
            ticks
            ):
        self.signal_symbol = signal_symbol
        self.threshold_price = threshold_price
        self.support_type = support_type
        self.trade_symbol = trade_symbol
        self.ticks = ticks
        self.__repr__ = self.__str__

    def onUpdate():
        pass

    def onTrade(self, time, price, size, side):
        pass

    def __str__(self):
        return  (str(self.signal_symbol) + " "
                + str(self.threshold_price) + " "
                + str(self.support_type) + " "
                + str(self.trade_symbol) + " "
                + str(self.ticks))

bounces = []

bounces.append(BounceTrade("DKNG", 46.00, SupportType.Low, BounceOption("DKNG", "C", "20211029", 48.00), 0.10))

for b in bounces:
    print(b)

###### TODO ######
# 3. Subscribe to market data
# 4. Make a trade
# 5. Track position
# 6. Exit position
