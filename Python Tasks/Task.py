# Task.py
a=5
b=6
print("a&b", a&b)

a=10
b=12
print("a&b", a&b)


# a=15
# b=16
# print("a&b", a&b)

# a=5
# b=6
# print("a|b", a|b)

# a=10
# b=12
# print("a|b", a|b)

# a=13
# b=14
# print("a|b", a|b)


# a=5
# b=6
# print("a^b", a^b)

# a=18
# b=19
# print("a^b", a^b)

# a=22
# b=24
# print("a^b", a^b)




# print("-----MENU------")
# ch=str(input("""
# 1.Biryani
# 2.Chicken 65
# 3.Veg Pulao
# 4.Butter Chicken
# 5.Paneer Tikka
# Enter Your Choise:"""))

# match ch:
#     case "1":
#         print("""
#         item       :Biryani
#         price      :$100
#         Description: Crispy And Spicy""")
#     case "2":
#         print("""
#         item       :Chicken 65
#         price      :$180
#         Description: Crispy And Spicy deep fried chicken""")
#     case "3":
#         print("""
#         item       :Veg Pulao
#         price      :$130
#         Description: minimum spicy with extra onions""")
#     case "4":
#         print("""
#         item       :Butter Chicken
#         price      :$230
#         Description: extra butter """)
#     case "5":
#         print("""
#         item       :Paneer Tikka
#         price      :$260
#          Description: spicy with roasted pannner""")
#     case _:
#         print("sorry your order is invalid")




print("----- ATM MENU------")
ch=str(input("""
1.Check Balance
2.Deposit
3.Withdraw
4.Exit
Enter Your Choise:"""))

match ch:
    case "1":
        print("""
       Current Balance : 500""")
    case "2":
        ch=str(input("Enter Deposit Amount:"))
        print("Amount Deposited Successfully")
    case "3":
        ch=str(input("Enter Withdrawal Amount:"))
        print("""
        Withdrawal Successfully
        Remaining Balance: 5000""")
    case "4":
        print("Thankyou For Visting")
    case _:
        print("Invalid Choise")