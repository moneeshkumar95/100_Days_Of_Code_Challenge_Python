print('Day 36: Find the Armstrong Number')

print("\n-------------Approach 1-------------")
def armCheck1(n):
    total = [int(i) ** len(str(n)) for i in str(n)]
    if sum(total) == n:
        return f'{n} is an Armstrong Number'
    return f'{n} is not an Armstrong Number'

num1 = int(input("Enter a number: "))
print('\nOutput:',armCheck1(num1))

print("\n-------------Approach 2-------------")
def armCheck2(n):
    new, total2 = n, 0
    while new > 0:
        digit = new % 10
        total2 += digit ** len(str(n))
        new //= 10

    if total2 == n:
        return f'{n} is an Armstrong Number'
    return f'{n} is not an Armstrong Number'

num2 = int(input("Enter a number: "))
print('\nOutput:',armCheck2(num2))