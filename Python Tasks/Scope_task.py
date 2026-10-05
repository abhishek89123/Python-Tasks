bank = "SBI"  # Global variable

def account():
    account_type = "Savings"  # Enclosing variable

    def customer():
        balance = 50000 
        print(balance)      
        print(account_type)  
        print(bank)          

        def transaction():
            amount = 2500
            print(amount)        
            print(account_type)  
            print(bank)          
        transaction()
    customer()
account()
