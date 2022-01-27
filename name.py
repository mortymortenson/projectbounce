import vwap
import datetime

class Name(object):
    def __init__(self, symbol):
        self.symbol = symbol
        if hasattr(symbol, 'sid'):
            self.sid = symbol.sid

        # Historical values
        self.adv30Day = None
        self.prevClose = None
        self.openInterest = None
        self.ema21Day = None
        # etc....

        # Realtime values
        self.premarketLow = None
        self.premarketHigh = None
        self.premarketVolume = None

        self.openPrice = None
        self.openVolume = None

        self.vwap2s = vwap.TrailingVWAP(datetime.timedelta(seconds=2), datetime.timedelta(seconds=2)/10)
        self.vwap5s = vwap.TrailingVWAP(datetime.timedelta(seconds=5), datetime.timedelta(seconds=5)/10)
        self.vwap10s = vwap.TrailingVWAP(datetime.timedelta(seconds=10), datetime.timedelta(seconds=10)/10)
        self.vwap1m = vwap.TrailingVWAP(datetime.timedelta(minutes=1), datetime.timedelta(minutes=1)/10)
        self.vwap1h = vwap.TrailingVWAP(datetime.timedelta(hours=1), datetime.timedelta(hours=1)/10)

    def onTrade(self, time, price, size):
        self.vwap2s.onValue(time, price, size)
        self.vwap5s.onValue(time, price, size)
        self.vwap10s.onValue(time, price, size)
        self.vwap1m.onValue(time, price, size)
        self.vwap1h.onValue(time, price, size)

    def __str__(self):
        now = datetime.datetime.now()
        return (f"{self.symbol}"
                f" 2s: [ vwap: {self.vwap2s.getVWAP(now)} vol: {self.vwap2s.getVolume(now)} ]"
                f" 5s: [ vwap: {self.vwap5s.getVWAP(now)} vol: {self.vwap5s.getVolume(now)} ]"
                f" 10s: [ vwap: {self.vwap10s.getVWAP(now)} vol: {self.vwap10s.getVolume(now)} ]"
                f" 1m: [ vwap: {self.vwap1m.getVWAP(now)} vol: {self.vwap1m.getVolume(now)} ]"
                f" 1h: [ vwap: {self.vwap1h.getVWAP(now)} vol: {self.vwap1h.getVolume(now)} ]"
                )

if __name__ == '__main__':
    name = Name('AAPL')
    print('AAPL', str(name))

