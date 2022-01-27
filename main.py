import name
from ibapi.client import EClient
import ib

class TradingApp(ib.BApp):
    def __init__(self):
        ib.BApp.__init__(self)

    def start(self):
        pass

    def stop(self):
        pass

if __name__ == '__main__':
    ib.main(TradingApp)
