def max_risk_check(account_value, position_size, max_risk_pct=0.03):
    return position_size <= account_value * max_risk_pct