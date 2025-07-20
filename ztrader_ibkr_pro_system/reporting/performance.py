def track_pnl(trades):
    pnl = sum([t['pnl'] for t in trades])
    return pnl