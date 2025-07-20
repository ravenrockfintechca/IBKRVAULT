ibkr_quant_system/
├── strategies/
│   └── aurora_strategy.py        # 信号函数（基于 AUDJPY/VIX）
├── executions/
│   └── ib_order.py               # IB连接与下单模块
├── risk/
│   └── risk_control.py           # 仓位风控模块（最大风险比控制）
├── notifier/
│   └── notify.py                 # 推送接口（示例中为 print，可扩展）
├── logs/
│   └── log.txt                   # 简易日志文件
├── main.py                       # 主控执行器（信号→风控→下单→推送）
