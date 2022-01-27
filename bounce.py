from symbols import *

class SupportType(Enum):
    Bounce = 1
    Reject = 2
    Breakout = 3
    Breakdown = 4

class BounceTrade:
    def __init__(
            self,
            ts,
            signalSymbol,
            thresholdPrice,
            supportType,
            tradeSymbol,
            ticks
            ):
        self.ts = datetime.datetime.strptime(ts, TS_FMT)
        self.signalSymbol = signalSymbol
        self.thresholdPrice = thresholdPrice
        self.supportType = supportType
        self.tradeSymbol = tradeSymbol
        self.ticks = ticks
        self.__repr__ = self.__str__

    def onUpdate():
        pass

    def onTrade(self, time, price, size, side):
        if self.supportType == SupportType.Bounce:
            if price <= self.thresholdPrice + self.ticks:
                self._notify(price)
        elif self.supportType == SupportType.Reject:
            if price >= self.thresholdPrice - self.ticks:
                self._notify(price)
        elif self.supportType == SupportType.Breakout:
            pass
        elif self.supportType == SupportType.Breakdown:
            pass

    def _notify(self, price):
        msg =(str(self.supportType) + " "
                + str(self.signalSymbol) + " "
                + str(self.thresholdPrice) + " "
                + str(self.tradeSymbol) + " "
                + "Last Trade: " + str(price))
        final = "* " + msg + " *"
        stars = "*" * len(final)
        print("\n" + stars + "\n" + final + "\n" + stars + "\n")

    def __str__(self):
        return  (self.ts.strftime(TS_FMT) + " - "
                + str(self.signalSymbol) + " "
                + str(self.thresholdPrice) + " "
                + str(self.supportType) + " "
                + str(self.tradeSymbol) + " "
                + str(self.ticks))
bounces = []

bounces.append(BounceTrade("2021-10-23 20:30:00", BounceEquity("DKNG"), 46.00, SupportType.Bounce, BounceOption("DKNG", Right.Call, "20211029", 48.00), 0.10))

if __name__ == "__main__":
    for b in bounces:
        print(b)

