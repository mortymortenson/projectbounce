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
            ticks: float
            ):
        self.ts = datetime.datetime.strptime(ts, TS_FMT)
        self.signalSymbol = signalSymbol
        self.thresholdPrice = thresholdPrice
        self.supportType = supportType
        self.tradeSymbol = tradeSymbol
        self.ticks = ticks
        self.orderSent = False
        self.__repr__ = self.__str__

    def onUpdate() -> None:
        pass

    def shouldPlaceOrder(self):
        return not self.orderSent

    def onOrderPlaced(self):
        self.orderSent = True

    def onTrade(self, time: datetime.datetime, price: float, size: float) -> TradeRequest:
        if self.supportType == SupportType.Bounce:
            if price <= self.thresholdPrice + self.ticks:
                self._notify(price)
            return TradeRequest(self.tradeSymbol, Action.Buy, 1, None)
        elif self.supportType == SupportType.Reject:
            if price >= self.thresholdPrice - self.ticks:
                self._notify(price)
            return TradeRequest(self.tradeSymbol, Action.Buy, 1, None)
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
        logger.info(stars)
        logger.info(final)
        logger.info(stars)

    def __str__(self) -> str:
        return  (self.ts.strftime(TS_FMT) + " - "
                + str(self.signalSymbol) + " "
                + str(self.thresholdPrice) + " "
                + str(self.supportType) + " "
                + str(self.tradeSymbol) + " "
                + str(self.ticks))
bounces = []

bounces.append(BounceTrade("2021-10-23 20:30:00", BounceEquity("DKNG"), 46.00, SupportType.Bounce, BounceOption("DKNG", Right.Call, "20211029", 48.00), 0.10))

def runTests():
    for b in bounces:
        print(b)

if __name__ == '__main__':
    runTests()

