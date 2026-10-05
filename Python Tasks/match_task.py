# 1.Restaurant Menu
# Write a Python program using match-case to display a restaurant menu with 5 food items. 
# Ask the user to select an option and display the selected item's name, price, and description. 
# For an invalid choice, display Invalid choice.

# Example:

# ----- MENU -----
# Biryani
# Chicken 65
# Veg Pulao
# Butter Chicken
# Paneer Tikka

# Enter your choice: 2

# Item       : Chicken 65
# Price      : ₹180
# Description: Crispy and spicy deep-fried chicken pieces.



# print("----- MENU -----")
# print("1. Biryani")
# print("2. Chicken 65")
# print("3. Veg Pulao")
# print("4. Butter Chicken")
# print("5. Paneer Tikka")

# choice=int(input("Enter your choice:"))

# match choice:
#     case 1:
#         print("Item       : Biryani")
#         print("Price      : ₹250")
#         print("Description: Fragrant basmati rice cooked with spicy chicken.")

#     case 2:
#         print("Item     : Chicken 65")
#         print("Price      : ₹180")
#         print("Description: Crispy and spicy deep-fried chicken pieces.")

#     case 3:
#         print("Item     : Veg Pulao")
#         print("Price      : ₹150")
#         print("Description: Flavourful rice cooked with fresh vegetables.")

#     case 4:
#         print("Item     : Butter Chicken")
#         print("Price      : ₹280")
#         print("Description: Tender chicken cooked in a creamy tomato gravy.")

#     case 5:
#         print("Item     : Paneer Tikka")
#         print("Price      : ₹200")
#         print("Description: Grilled paneer pieces marinated with spices.")

#     case _:
#         print("Invalid choice")
        
    # =================================================================================================================
    
#2. Write a Python program using match-case to create an ATM menu with 4 options. 
# Set the initial balance to ₹10,000, ask the user to select an option, and perform the 
# selected operation. For withdrawal, check whether sufficient balance is available. 
# For an invalid choice, display Invalid choice.

# Example:

# ----- ATM MENU -----
# Check Balance
# Deposit
# Withdraw
# Exit

# Enter your choice: 3
# Enter withdrawal amount: 3000

# Withdrawal successful.
# Remaining Balance: ₹7000

current_balance=int(10000)

print("1.Check Balance")
print("2.Diposit")
print("3.Withdrawl")
print("4.Exit")
choice=int(input("Enter your Choice :"))

match choice:
    case 1:
        print(current_balance)
    case 2:
        diposit_Amount=int(input("Enter the Diposit Amount :"))
        print("Current Balance =" ,current_balance+diposit_Amount)
    case 3:
        Withdrawl=int(input("Enter the Amount :"))
        print("Remaining Balance = ",current_balance-Withdrawl)
    case 4:
        print("Dear Customer, Visit Again")
        print("Exit Successfully")
    case _:
        print("Invalid Option")
        print("Try Again")