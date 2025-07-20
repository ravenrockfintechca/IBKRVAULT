def route_signals(strategies, data):
    signals = {}
    for name, strategy in strategies.items():
        signals[name] = strategy(data)
    return signals