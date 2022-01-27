import name
from ibapi.client import EClient
from ib import *
import bounce
import symbols
import name
import logging
import collections
import context

logger = logging.getLogger()

class TradingApp(BApp):
    def __init__(self):
        BApp.__init__(self)
        self.config = bounce.bounces

        self.symbolBounces = symbols.getSIDList(default=set)
        self.signalSymbols = symbols.getSIDList()
        self.tickRequests = {}
        self.nextRequestId = 1000

        for b in self.config:
            print(b)

            sid = b.signalSymbol.sid
            if not self.signalSymbols.get(sid):
                self.signalSymbols[sid] = name.Name(b.signalSymbol)

            self.symbolBounces[sid].add(b)

    # Override
    def start(self):
        self.reqMarketDataType(MarketDataTypeEnum.DELAYED)
        self.subscribeMarketData()

    # Override
    def stop(self):
        logger.info("Unsubscribing from all market data")
        for requestId in self.tickRequests:
            self.cancelTickByTickData(requestId)

    def subscribeMarketData(self):
        for name in self.signalSymbols:
            if not name:
                continue
            logger.info("Subscribing to market data for %s (%d)", name.symbol, self.nextRequestId)

            # TODO - this uses TickByTick data; we can also get 250ms snapshots with reqMktData

            self.reqTickByTickData(self.nextRequestId, name.symbol, "Last", 0, True)
            self.tickRequests[self.nextRequestId] = name
            self.nextRequestId += 1

    @iswrapper
    # ! [tickbytickalllast]
    def tickByTickAllLast(self, reqId: int, tickType: int, time: int, price: float,
                          size: int, tickAtrribLast: TickAttribLast, exchange: str,
                          specialConditions: str):
        super().tickByTickAllLast(reqId, tickType, time, price, size, tickAtrribLast,
                                  exchange, specialConditions)
        name = self.tickRequests.get(reqId)
        if not name:
            logger.warn("Got tick callback for unknown request %s", reqId)
            return

        now = context.now()

        logger.info("Trade %s %s %s %s %s", now, time, price, size)
        name.onTrade(now, price, size)

        self.checkBounces(now, name, price, size)

    def checkBounces(self, now, name, price, size):
        bounces = self.symbolBounces.get(name.sid)
        if not bounces:
            return

        for b in bounces:
            b.onTrade(now, price, size, None)

if __name__ == '__main__':
    context.init()
    a = TradingApp()
    a.start()
    a.tickByTickAllLast(1000, 1, 123456, 46.5,  100, TickAttribLast(), "ISLAND", "cond")
    a.tickByTickAllLast(1000, 1, 123456, 46.11, 100, TickAttribLast(), "ISLAND", "cond")
    a.tickByTickAllLast(1000, 1, 123456, 46.1,  100, TickAttribLast(), "ISLAND", "cond")
    a.tickByTickAllLast(1000, 1, 123456, 46.01, 100, TickAttribLast(), "ISLAND", "cond")
    a.tickByTickAllLast(1000, 1, 123456, 45.00, 100, TickAttribLast(), "ISLAND", "cond")
    a.tickByTickAllLast(1000, 1, 123456, 46.11, 100, TickAttribLast(), "ISLAND", "cond")
    # context.init()
    # ib.main(TradingApp)
