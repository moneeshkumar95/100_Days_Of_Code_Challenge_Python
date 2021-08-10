#Day 10 : Prints each number from 1 to n(user input) on a new line - [FizzBuzz]

print("---------Approach 1---------")
num1 = int(input("Enter a number: "))
for i in range(1, num1+1):
    if i%3 ==0 and i%5 == 0:
        print("FizzBuzz")
    elif i%3 == 0:
        print("Fizz")
    elif i%5 == 0:
        print("Buzz")
    else:
        print(i)

print("\n---------Approach 2---------")
num2 = int(input("Enter a number: "))
print(*map(lambda i: 'Fizz'*(not i%3)+'Buzz'*(not i%5) or i, range(1,num2+1)),sep='\n')