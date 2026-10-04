# # TASK #
# #find avg of first n natural number using for loop
# n=int(input("Enter a Number ="))
# sum=0
# for i in range(1,n+1,1):
#     sum=sum+i
# avg=sum/n
# print(f"Average of {n} natural number is={avg}")


# # 2.Find the sum of squares of numbers from 1 to N.
# n=int(input("Enter a number "))
# sum=0
# for i in range(1,n+1,1):
#     sum=sum+i ** 2
# print("Sum of squares",sum)


# # 3.Find the sum of cubes of numbers from 1 to N.
# n=int(input("Enter a number ="))
# sum=0
# for i in range(1,n+1,1):
#     sum=sum+i**3
# print(f"sum of cubes is {sum}")

# #4.Calculate the power of a number without using the ** operator.
# base=int(input("Enter base number ="))
# power=int(input("Enter power number ="))
# result=1
# for i in range(1,power+1,1):
#     result=result*base
# print(result)


# # 5.Display the first N terms of the Fibonacci series.
# n=5
# a=0
# b=1
# print("Fibonacci series =")
# for i in range(1,n+1,1):
#     print(a,end=" ")
#     c=a+b
#     a=b
#     b=c

# # 6.Display the first N terms of the series: 1, 1/2, 1/3, 1/4, ...
# #     Example: If N = 4, display 1, 1/2, 1/3, 1/4.


# # n=int(input("Enter number ="))
# # start=1
# # print(start)
# # for i in range(2,n+1,1):
# #     print(f"1/{i}")

# n=int(input("enter a number ="))
# for i in range(1,n+1,1):
#     if(1%i==0):
#         print(i,end=" ")
#     else:
#         print(f"1/{i}",end=" ")


# # 7.Display the first N terms of the series:
# #     1, 11, 111, 1111, 11111, ...
# #     Example: If N = 5, display 1, 11, 111, 1111, 11111.0
# n=int(input("Enter a number"))
# series=""
# print("first N terms of the series :")
# for i in range(1,n+1,1):
#     series=series+"1"
#     print(series,end=" ")


# #8.Display the first N terms of the series:
#     # 1, 3, 9, 27, 81, ...
#     # Each term is obtained by multiplying the previous term by 3
# n=5
# a=1
# for i in range(1,n+1,1):
#     print(a)
#     a=a*3
