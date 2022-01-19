import vwap
import datetime

class Name(object):
    def __init__(self, symbol):
        self.symbol = symbol
        # Historical values
        self.adv_30_day = None
        self.prev_close = None
        self.open_interest = None
        self.ema_21_day = None
        # etc....

        # Realtime values
        self.premarket_low = None
        self.premarket_high = None
        self.premarket_volume = None

        self.open_price = None
        self.open_volume = None

        self.vwap_2s = vwap.TrailingVWAP(datetime.timedelta(seconds=2), datetime.timedelta(seconds=2)/10)
        self.vwap_5s = vwap.TrailingVWAP(datetime.timedelta(seconds=5), datetime.timedelta(seconds=5)/10)
        self.vwap_10s = vwap.TrailingVWAP(datetime.timedelta(seconds=10), datetime.timedelta(seconds=10)/10)
        self.vwap_1m = vwap.TrailingVWAP(datetime.timedelta(minutes=1), datetime.timedelta(minutes=1)/10)
        self.vwap_1h = vwap.TrailingVWAP(datetime.timedelta(hours=1), datetime.timedelta(hours=1)/10)

    def __str__(self):
        now = datetime.datetime.now()
        return (f"{self.symbol}"
                f" 2s: [ vwap: {self.vwap_2s.getVWAP(now)} vol: {self.vwap_2s.getVolume(now)} ]"
                f" 5s: [ vwap: {self.vwap_5s.getVWAP(now)} vol: {self.vwap_5s.getVolume(now)} ]"
                f" 10s: [ vwap: {self.vwap_10s.getVWAP(now)} vol: {self.vwap_10s.getVolume(now)} ]"
                f" 1m: [ vwap: {self.vwap_1m.getVWAP(now)} vol: {self.vwap_1m.getVolume(now)} ]"
                f" 1h: [ vwap: {self.vwap_1h.getVWAP(now)} vol: {self.vwap_1h.getVolume(now)} ]"
                )

if __name__ == '__main__':
    name = Name('AAPL')
    print('AAPL', str(name))

