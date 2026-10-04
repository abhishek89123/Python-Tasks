# 1.Find the sum of digits in a given number.
#     Example: 738 → 7 + 3 + 8 = 18

# n=738
# sum=0
# while n!=0:
#     ld=n%10
#     sum=sum+ld
#     n=n//10
# print(sum)


# 2.Find the average of digits in a given number.
#      Example: 624 → (6 + 2 + 4) / 3 = 4

# n=624
# sum=0
# count=0
# while n!=0:
#     ld=n%10
#     sum=sum+ld
#     count+=1
#     avg=sum/count
#     n=n//10
# print(avg)


# 3.Find the sum of the first digit and the last digit of a given number.
#      Example: 936 → 9 + 6 = 15

# n=936
# ld=n%10
# while n>9:
#     n=n//10
# first=n
# print(first+ld)

#4.Find the average of digits that are divisible by 5 in a given number.
# Example: 12575 → Divisible by 5 digits: 5, 5, 5 → Average = (5 + 5 + 5) / 3 = 5

n=int(input("enter any  number : "))

sum=0
count=0
while n!=0:
    digit=n %10
    if digit%5==0:
        count+=1
        sum=sum+digit
    n=n//10
print(f"Avg of the 5 divisibles ={sum/count}")

#5.Find the difference between the largest digit and the smallest digit in a given number.
 #    Example: 58321 → Largest = 8, Smallest = 1 → Difference = 8 - 1 = 7
 
n=int(input("enter any number : "))

largest=0
smallest=9
while n!=0:
    digit=n % 10
    if digit> largest:
        largest=digit
    if digit<=smallest:
        smallest=digit
    n=n//10
print(f"Difference between the given number {largest} - {smallest} = {largest-smallest}")