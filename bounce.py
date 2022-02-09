from symbols import *
from util import *
import datetime
import logging

logger = logging.getLogger()

class SupportType(Enum):
    Bounce = 1
    Reject = 2
    Breakout = 3
    Breakdown = 4

class BounceTrade:
    def __init__(
            self,
            ts: datetime.datetime,
            signalSymbol: str,
            thresholdPrice: float,
            supportType: SupportType,
            tradeSymbol: BounceSymbol,
            ticks: float,
            actuallySendOrder: bool=False
            ):
        self.ts = datetime.datetime.strptime(ts, TS_FMT)
        self.signalSymbol = signalSymbol
        self.thresholdPrice = thresholdPrice
        self.supportType = supportType
        self.tradeSymbol = tradeSymbol
        self.ticks = ticks
        self.orderSent = False
        self.actuallySendOrder = actuallySendOrder
        self.__repr__ = self.__str__

    def onUpdate() -> None:
        pass

    def shouldPlaceOrder(self):
        return not self.orderSent and self.actuallySendOrder

    def onOrderPlaced(self):
        self.orderSent = True

    def onTrade(self, time: datetime.datetime, price: float, size: float) -> TradeRequest:
        if self.supportType == SupportType.Bounce:
            if price <= self.thresholdPrice + self.ticks:
                self._notify(price)
                return TradeRequest(self.tradeSymbol, Action.Buy, None, 1)
        elif self.supportType == SupportType.Reject:
            if price >= self.thresholdPrice - self.ticks:
                self._notify(price)
                return TradeRequest(self.tradeSymbol, Action.Buy, None, 1)
        elif self.supportType == SupportType.Breakout:
            pass
        elif self.supportType == SupportType.Breakdown:
            pass

    def _notify(self, lastTradePrice: float) -> None:
        msg =(str(self.supportType) + " "
                + str(self.signalSymbol) + " "
                + str(self.thresholdPrice) + " "
                + str(self.tradeSymbol) + " "
                + "Last Trade: " + str(lastTradePrice))
        final = "* " + msg + " *"
        stars = "*" * len(final)
        logger.info(logColor(stars, LogCyan))
        logger.info(logColor(final, LogCyan))
        logger.info(logColor(stars, LogCyan))

    def __str__(self) -> str:
        return  (self.ts.strftime(TS_FMT) + " - "
                + str(self.signalSymbol) + " "
                + str(self.thresholdPrice) + " "
                + str(self.supportType) + " "
                + str(self.tradeSymbol) + " "
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

def runTests():
    for b in bounces:
        print(b)

if __name__ == '__main__':
    runTests()

