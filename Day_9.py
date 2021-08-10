#Day 9: Check whether a number is prime or not

print("\n---Prime Number or Not---")
def checker(n):
    no_of_divisible = 0
    for i in range(1, n+1):
        if n%i == 0:
            no_of_divisible += 1
    if no_of_divisible == 2:
        return f"{num} is a prime number"
    return f"{num} is not prime number"

num = int(input("Enter a number: "))
print(checker(num))