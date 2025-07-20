from strategies.sample_strategy import generate_signal
from executions.order_executor import connect_ib, place_order
from risk.evaluator import risk_ok
from notifier.dispatcher import send_notification
from monitor.account_status import check_account

# Simulated market data
data = {'close': [99, 100, 102, 101, 103]}

signal = generate_signal(data)
ib = connect_ib()
account_value = 100000
trade_risk = 2000

if signal == 1 and risk_ok(account_value, trade_risk):
    contract = Forex('AUDJPY')
    order = place_order(ib, contract, 'BUY', 10000)
    send_notification("Long AUDJPY executed.")