# 主控调度器 main.py

from strategies.alpha_signal import generate_alpha_signal
from router.signal_router import route_signal
from executions.order_executor import place_order
from risk.evaluator import check_risk
from monitor.account_status import get_account_info
from notifier.dispatcher import send_notification
from infra.recovery import reconnect
from data.data_loader import load_data

def main():
    try:
        data = load_data()
        signal = generate_alpha_signal(data)
        if check_risk():
            route_signal()
            place_order(signal)
            send_notification("Signal executed.")
    except Exception as e:
        send_notification(f"Error occurred: {e}")
        reconnect()

if __name__ == "__main__":
    main()