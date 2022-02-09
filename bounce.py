from enum import Enum
from ibapi.contract import *
import datetime

TS_FMT = "%Y-%m-%d %H:%M:%S"

class Action(Enum):
    Buy = 1
    Sell = 2

class SupportType(Enum):
    Bounce = 1
    Reject = 2
    Breakout = 3
    Breakdown = 4

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
            ts,
            signal_symbol,
            threshold_price,
            support_type,
            trade_symbol,
            ticks
            ):
        self.ts = datetime.datetime.strptime(ts, TS_FMT)
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
        return  (self.ts.strftime(TS_FMT) + " - "
                + str(self.signal_symbol) + " "
                + str(self.threshold_price) + " "
                + str(self.support_type) + " "
                + str(self.trade_symbol) + " "
                + str(self.ticks))

bounces = []

bounces.append(BounceTrade("2021-10-25 20:30:00", "DKNG", 46.00, SupportType.Bounce, BounceOption("DKNG", "C", "20211029", 48.00), 0.10))
bounces.append(BounceTrade("2021-10-25 8:30:00", "EBAY", 79.30, SupportType.Bounce, BounceOption("EBAY", "C", "20211029", 84.00), 0.10))
bounces.append(BounceTrade("2021-10-25 8:30:00", "MARA", 49.50, SupportType.Bounce, BounceOption("MARA", "C", "20211029", 52.00), 0.10))
bounces.append(BounceTrade("2021-10-25 8:40:00", "NVDA", 229.00, SupportType.Bounce, BounceOption("NVDA", "C", "20211029", 235.00), 0.10))
bounces.append(BounceTrade("2021-10-25 8:48:00", "XPEV", 44.00, SupportType.Bounce, BounceOption("XPEV", "C", "20211029", 45.00), 0.10))
bounces.append(BounceTrade("2021-10-23 8:50:00", "AFRM", 153.50, SupportType.Bounce, BounceOption("AFRM", "C", "20211029", 160.00), 0.10))
bounces.append(BounceTrade("2021-10-25 9:00:00", "NFLX", 660.00, SupportType.Bounce, BounceOption("NFLX", "C", "20211029", 670.00), 0.10))
bounces.append(BounceTrade("2021-10-25 9:30:00", "TSLA", 942.00, SupportType.Bounce, BounceOption("TSLA", "C", "20211029", 950.00), 0.10))
bounces.append(BounceTrade("2021-10-25 9:30:00", "PYPL", 251.00, SupportType.Bounce, BounceOption("PYPL", "C", "20211029", 250.00), 0.10))
bounces.append(BounceTrade("2021-10-25 9:30:00", "X", 22.90, SupportType.Bounce, BounceOption("X", "C", "20211029", 24.00), 0.10))
bounces.append(BounceTrade("2021-10-25 20:30:00", "NVDA", 242.00, SupportType.Bounce, BounceOption("NVDA", "C", "20211029", 250.00), 0.10))
bounces.append(BounceTrade("2021-10-27 9:20:00", "TSLA", 1020.00, SupportType.Bounce, BounceOption("TSLA", "C", "20211029", 1100.00), 0.10))
bounces.append(BounceTrade("2021-10-27 9:20:00", "NVDA", 242.00, SupportType.Bounce, BounceOption("X", "C", "20211029", 24.00), 0.10))
bounces.append(BounceTrade("2021-10-27 9:20:00", "MSFT", 310.00, SupportType.Bounce, BounceOption("MSFT", "C", "20211029", 320.00), 0.10))
bounces.append(BounceTrade("2021-10-24 20:30:00", "NVDA", 242.00, SupportType.Bounce, BounceOption("X", "C", "20211029", 24.00), 0.10))
bounces.append(BounceTrade("2021-10-27 9:20:00", "BA", 213.00, SupportType.Bounce, BounceOption("BA", "C", "20211029", 220.00), 0.10))
bounces.append(BounceTrade("2021-11-02 9:15:00", "UPST", 343.50, 340.00, SupportType.Bounce, BounceOption("UPST", "C", "20211105", 350.00), 0.10))
bounces.append(BounceTrade("2021-11-02 9:15:00", "TSLA", 1140.00, 1130.00, SupportType.Bounce, BounceOption("TSLA", "C", "20211105", 1200.00), 0.10))
bounces.append(BounceTrade("2021-11-02 9:15:00", "DM", 8.40, 8.00, SupportType.Bounce, BounceOption("DM", "C", "20211105", 9.00), 0.10))
bounces.append(BounceTrade("2021-11-02 9:20:00", "MCD", 250.00, SupportType.Bounce, BounceOption("MCD", "C", "20211105", 252.50), 0.10))
bounces.append(BounceTrade("2021-10-27 9:20:00", "AMD", 123.00, SupportType.Bounce, BounceOption("AMD", "C", "20211105", .00), 0.10))
bounces.append(BounceTrade("2021-10-27 9:20:00", "BA", 212.00, SupportType.Bounce, BounceOption("BA", "C", "20211105", 215.00), 0.10))
bounces.append(BounceTrade("2021-11-08 8:40:00", "V", 217.00, SupportType.Bounce, BounceOption("V", "C", "20211112", 220.00), 0.10))
bounces.append(BounceTrade("2021-11-08 8:40:00", "AMD", 136.30, SupportType.Bounce, BounceOption("AMD", "C", "20211112", 140.00), 0.10))
bounces.append(BounceTrade("2021-11-08 8:40:00", "BA", 224.00, SupportType.Bounce, BounceOption("BA", "C", "20211112", 230.00), 0.10))
bounces.append(BounceTrade("2021-11-08 9:00:00", "ABNB", 200.00, SupportType.Bounce, BounceOption("ABNB", "C", "20211112", 210.00), 0.10))
bounces.append(BounceTrade("2021-11-09 9:20:00", "AMD", 150.00, SupportType.Bounce, BounceOption("AMD", "C", "20211112", 150.00), 0.10))
bounces.append(BounceTrade("2021-11-08 9:00:00", "ABNB",200.00, SupportType.Bounce, BounceOption("ABNB", "C", "20211112", 210.00), 0.10))
bounces.append(BounceTrade("2021-11-08 9:20:00", "NVDA", 321.00, SupportType.Bounce, BounceOption("NVDA", "C", "20211112", 330.00), 0.10))
bounces.append(BounceTrade("2021-11-08 9:00:00", "NVDA",316.00, SupportType.Bounce, BounceOption("NVDA", "C", "20211112", 330.00), 0.10))
bounces.append(BounceTrade("2021-11-08 9:00:00", "TTD", 85.00, SupportType.Bounce, BounceOption("TTD", "C", "20211112", 90.00), 0.10))
bounces.append(BounceTrade("2021-11-08 9:00:00", "ABNB",200.00, SupportType.Bounce, BounceOption("ABNB", "C", "20211112", 210.00), 0.10))
bounces.append(BounceTrade("2021-11-11 9:00:00", "AFRM",165.00, SupportType.Bounce, BounceOption("AFRM", "C", "20211112", 180.00), 0.10))
bounces.append(BounceTrade("2021-11-11 9:00:00", "TSLA",1070.00, SupportType.Bounce, BounceOption("TSLA", "C", "20211112", 1200.00), 0.10))
bounces.append(BounceTrade("2021-11-08 9:00:00", "MA",354.50, SupportType.Bounce, BounceOption("MA", "C", "20211112", 360.00), 0.10))
bounces.append(BounceTrade("2021-11-29 9:00:00", "MRNA",350.00, SupportType.Bounce, BounceOption("MRNA", "C", "20211203", 375.00), 0.10))
bounces.append(BounceTrade("2021-11-29 9:00:00", "AAPL",158.50, SupportType.Bounce, BounceOption("AAPL", "C", "20211203", 165.00), 0.10))
bounces.append(BounceTrade("2021-12-22 9:00:00", "TSLA",960.00, SupportType.Bounce, BounceOption("TSLA", "C", "20211223", 980.00), 0.10))
bounces.append(BounceTrade("2021-11-29 9:00:00", "AMD",140.50, SupportType.Bounce, BounceOption("AMD", "C", "20211223", 145.00), 0.10))
bounces.append(BounceTrade("2021-11-29 9:00:00", "BA",206.50, SupportType.Bounce, BounceOption("BA", "C", "20211223", 205.00), 0.10))
bounces.append(BounceTrade("2021-12-27 9:20:00", "TSLA",1060.00, SupportType.Bounce, BounceOption("TSLA", "C", "20211231", 1100.00), 0.10))
bounces.append(BounceTrade("2021-12-27 9:20:00", "FB",336.00, SupportType.Bounce, BounceOption("FB", "C", "20211231", 340.00), 0.10))


for b in bounces:
    print(b)

###### TODO ######
# 3. Subscribe to market data
# 4. Make a trade
# 5. Track position
# 6. Exit position
