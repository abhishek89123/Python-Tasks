bank = "SBI"  # Global variable

def account():
    account_type = "Savings"  # Enclosing variable

    def customer():
        balance = 50000  # Local variable
        print(balance)       # Local
        print(account_type)  # Enclosing
        print(bank)          # Global

        def transaction():
            amount = 2500
            print(amount)        # Local
            print(account_type)  # Enclosing
            print(bank)          # Global
        transaction()
    customer()
account()