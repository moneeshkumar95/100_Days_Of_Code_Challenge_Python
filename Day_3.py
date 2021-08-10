#Day 3 : Find the factorial of a given number

print("---------Method 1---------")
num = int(input("Enter the number: "))
fact = 1
for i in range(1,num+1):
    fact *= i
print(f"The factorial of {num} is {fact}")

print("\n---------Method 2---------")
num = int(input("Enter the number: "))
def fact(num):
    return 1 if (num<=1) else num*fact(num-1)
print(f"The Factorial of {num} is {fact(num)}")

print("\n---------Method 3---------")
import math
num = int(input("Enter the number: "))
def fact_m(num):
    return math.factorial(num)
print(f"The Factorial of {num} is {fact_m(num)}")

