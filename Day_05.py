#Day 5 : Reverse the given number.
print("\n---------Method 1---------")
num1 = input("Enter the numbers: ")
print("The reversed number is",num1[::-1])

print("\n---------Method 2---------")
num2 = int(input("Enter the numbers: "))
result2 = 0
while (num2>0):
    remainder = num2 % 10
    result2 = (result2 * 10) +remainder
    num2 = num2 // 10
print("The reversed number is", result2)

print("\n---------Method 3---------")
num3 = list(input("Enter the numbers: "))
result3 = ""
for i in num3[::-1]:
    result3 += i
print("The reversed number is",result3)



