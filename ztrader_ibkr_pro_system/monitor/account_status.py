def check_account(account_data):
    # basic balance check
    return {
        'equity': account_data['NetLiquidation'],
        'margin': account_data['AvailableFunds']
    }