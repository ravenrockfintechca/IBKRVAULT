from strategies.aurora_strategy import aurora_signal
from executions.ib_order import connect_ib, place_order
from notifier.notify import notify
from risk.risk_control import max_risk_check

# 模拟数据输入
audjpy = 96.8
vix = 14.2
account_value = 10000
size = 3000

signal = aurora_signal(audjpy, vix)
ib = connect_ib()

if signal == 1 and max_risk_check(account_value, size):
    place_order(ib, 'BUY', size)
    notify("Entered long AUDJPY")
elif signal == -1 and max_risk_check(account_value, size):
    place_order(ib, 'SELL', size)
    notify("Entered short AUDJPY")
else:
    notify("No signal or risk too high")