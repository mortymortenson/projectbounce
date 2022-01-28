import name
from ibapi.client import EClient
from ib import *
import bounce
import util
import symbols
import name
import logging
import collections
import context

logger = logging.getLogger()

class BounceApp(BApp):
    def __init__(self):
        BApp.__init__(self)
        self.config = bounce.bounces

        self.symbolBounces = symbols.getSIDList(default=set)
        self.signalSymbols = symbols.getSIDList()
        self.tickRequests = {}
        self.nextRequestId = 1000

        for b in self.config:
            logger.info("Adding bounce config %s", b)

            sid = b.signalSymbol.sid
            if not self.signalSymbols.get(sid):
                self.signalSymbols[sid] = name.Name(b.signalSymbol)

            self.symbolBounces[sid].add(b)

    # Override
    def start(self) -> None:
        self.reqMarketDataType(MarketDataTypeEnum.DELAYED)
        self.subscribeMarketData()

    # Override
    def stop(self) -> None:
        logger.info("Unsubscribing from all market data")
        for requestId in self.tickRequests:
            self.cancelTickByTickData(requestId)

    def subscribeMarketData(self) -> None:
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
                          specialConditions: str) -> None:
        super().tickByTickAllLast(reqId, tickType, time, price, size, tickAtrribLast,
                                  exchange, specialConditions)
        name = self.tickRequests.get(reqId)
        if not name:
            logger.warn("Got tick callback for unknown request %s", reqId)
            return

        now = context.now()

        logger.info("Trade %s %s %s %s", now, time, price, size)
        name.onTrade(now, price, size)

        self.checkBounces(now, name, price, size)

    def checkBounces(self, now: datetime.datetime, name: name.Name, price: float, size: float) -> None:
        bounces = self.symbolBounces.get(name.sid)
        if not bounces:
            return

        for b in bounces:
            request = b.onTrade(now, price, size)
            if request:
                if request.price is None:
                    spec = MarketOrder(request.action, request.size)
                else:
                    spec = LimitOrder(request.action, request.size, request.price)
                if b.shouldPlaceOrder():
                    self.doOrderPlacement(request.contract, spec)
                    b.onOrderPlaced()

    def doOrderPlacement(self, contract:symbols.BounceSymbol, spec: Order) -> None:
        oid = self.nextOrderId()
        priceStr = ""
        if spec.orderType == "LMT":
            priceStr = str(spec.lmtPrice)
        logger.info("Sending Order: %s %s %s %s %s",
                oid,
                contract,
                spec.totalQuantity,
                spec.orderType,
                priceStr)

        self.placeOrder(oid, contract, spec)

def runTests():
    context.init()
    a = BounceApp()
    a.nextValidId(1)
    a.start()
    a.tickByTickAllLast(1000, 1, 123456, 46.5,  100, TickAttribLast(), "ISLAND", "cond")
    a.tickByTickAllLast(1000, 1, 123456, 46.11, 100, TickAttribLast(), "ISLAND", "cond")
    a.tickByTickAllLast(1000, 1, 123456, 46.1,  100, TickAttribLast(), "ISLAND", "cond")
    a.tickByTickAllLast(1000, 1, 123456, 46.01, 100, TickAttribLast(), "ISLAND", "cond")
    a.tickByTickAllLast(1000, 1, 123456, 45.00, 100, TickAttribLast(), "ISLAND", "cond")
    a.tickByTickAllLast(1000, 1, 123456, 46.11, 100, TickAttribLast(), "ISLAND", "cond")

if __name__ == '__main__':
    util.setupLogger()
    runTests()

