from ib_insync import *

def connect_ib():
    ib = IB()
    ib.connect('127.0.0.1', 7497, clientId=1)
    return ib

def place_order(ib, contract, action, quantity):
    order = MarketOrder(action, quantity)
    ib.placeOrder(contract, order)
    return order