print('Day 38: Find minimum sum of factors of number\n')

def check(num):
    sum_min = 0

    i = 2
    while i * i <= num:
        while num % i == 0:
            sum_min += i
            num //= i
        i += 1
    sum_min += num

    return sum_min

number = int(input('Enter a number: '))
print(f'\nMinimum sum factor of {number} is {check(number)}')
