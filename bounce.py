from enum import Enum
from ibapi.contract import Option

class Action(Enum):
    Buy = 1
    Sell = 2

class SupportType(Enum):
    Low = 1
    High = 2

class Option:
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
        return contract

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
        self.treshold_price = threshold_price
        self.support_type = support_type
        self.trade_symbol = trade_symbol
        self.ticks = ticks

    def onUpdate():
        pass

    def onTrade(self, time, price, size, side):
        pass

    def __str__(self):
        print(self.signal_symbol,
                self.threshold_price,
                self.support_type,
                self.trade_symbol,
                self.ticks = ticks)

bounces = []

bounces.append(BounceTrade("DKNG", 46.00, SupportType.Low, Option("DKNG", "C", "20211029", 48.00), 0.10))

for b in bounce:
    print(str(bounces))

###### TODO ######
# 3. Subscribe to market data
# 4. Make a trade
# 5. Track position
# 6. Exit position
