#100 days of python coding challenge
#Day 4 : Find the area of a circle
import math

print("\n---------Method 1---------")
num = int(input("Enter the number: "))
area1 = math.pi * (num**2)
print( f"Area of the circle is {area1:.2f}")

print("\n---------Method 2---------")
def area(num):
    return 3.14159265359 * (num**2)
num = int(input("Enter the number: "))
print( f"Area of the circle is {area(num):.2f}")