def auto_reconnect(ib):
    if not ib.isConnected():
        ib.connect('127.0.0.1', 7497, clientId=1)