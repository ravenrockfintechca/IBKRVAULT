def generate_signal(data):
    # placeholder for multi-factor strategy
    return 1 if data['close'][-1] > data['close'][-5] else 0