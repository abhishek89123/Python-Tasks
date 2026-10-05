# Without Input & Without Return

#1.sum of 2 numbers
# def add2():
#     a=10
#     b=20
#     sum=a+b
#     print("sum of",a,b,"is",sum)
# add2()

# 2.even or odd
# def even_odd():
#     n=2
#     if n%2==0:
#         print("even")
#     else:
#         print("Odd")
# even_odd()

#3.Positive or negative
# def positive_or_negative():
#     n=int(input("Enter any number :"))
#     if n>0:
#         print("given",n," is Positive")
#     else:
#         print("given",n," is  Negetive")
# positive_or_negative()


# 4.Biggest number
# def big():
#     a = 10
#     b = 50
#     c = 30
#     if a > b and a > c:
#         print(a, "is big")
#     elif b > a and b > c:
#         print(b, "is big")
#     else:
#         print(c, "is big")
# big()


# 5.pattern

# def plus():
#     for j in range(1,6,1):
#         for i in range(1,6,1):
#             if(j==3) or (i==3):
#             # if(j%2!=0):
#                 print("*",end=" ")
#             else:
#                 print(" ",end=" ")
#         print()
# plus()

#6.check given character is alphabet or digit or symbol

# def ADS():
#     n=input("Enter a value ")
#     if (n>="A" and n<="Z" or n>="a" and n<="z"):
#         print("Alphabet")
#     elif(n>="0" and  n<="9") or (n>="-1" and  n<="-9"):
#         print("Digit")
#     else:
#         print("Symbol")
# ADS()


# Named Function – With Input & Without Return

#1.sum of 2 numbers
# def add2(a,b):
#     sum=a+b
#     print("sum of",a,b,"is",sum)
# add2(20,30)

# 2.Multiplication of number
# def multi(n):
#     print("Multiplication table of ",n)
#     for i in range(1,11,1):
#         print(n,"X",i ,"=",n * i)
# multi(2)
    
#3.check given character is alphabet or digit or symbol

# def ADS(n):
#     n=str(n)
#     if (n>="A" and n<="Z" or n>="a" and n<="z"):
#         print("Alphabet")
#     elif(n>="0" and  n<="9") or (n>="-1" and  n<="-9"):
#         print("Digit")
#     else:
#         print("Symbol")
# ADS(input("enter n "))


# 4.Factorial
# def fact(n):
#     for j in range(1,n+1,1):
#         n=j
#         fact=1
#         for i in range(n,0,-1):
#             fact=fact*i
#     print(f"Factorial of {n} = {fact}")
# fact(5)

# 5.Vowel or not
# def vowelornot(ch):
#     if ch=="A" or ch=="E"  or ch=="I" or ch=="O" or ch=="U" or ch=="a" or ch=="e"  or ch=="i" or ch=="o" or ch=="u":
#         print(ch,"is a vowel")
#     else:
#         print(ch,"is not a vowel")
# vowelornot(input("Enter a letter "))


#6.display grade

# def grade(n):
#     n=int(n)
#     if (n>90):
#         print("Grade O")
#     elif (n>=71 and n<=90):
#         print("Grade A")
#     elif (n>=50 and n<=70):
#         print("Grade B")
#     elif (n>=35 and n<50):
#         print("Grade C")
#     else:
#         print("Fail")
# grade(input("Enter n "))


