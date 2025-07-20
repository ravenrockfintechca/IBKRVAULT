def risk_ok(account_value, trade_risk, max_risk_pct=0.03):
    return trade_risk <= account_value * max_risk_pct