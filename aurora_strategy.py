def aurora_signal(audjpy, vix):
    signal = 0
    if audjpy >= 96 and audjpy < 100 and vix < 16:
        signal = 1  # 多头
    elif audjpy >= 107:
        signal = -1  # 做空
    return signal