from enum import Enum

class Action(Enum):
    Buy = 1
    Sell = 2

class Side(Enum):
    Bid = 1
    Ask = 2

class Right(Enum):
    Put = "P"
    Call = "C"

###### TODO ######
# 3. Subscribe to market data
# 4. Make a trade
# 5. Track position
# 6. Exit position
