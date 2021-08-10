print('Day 83\n')

def sqrtFinder(num):

    if num < 0:
        raise ValueError
    elif num == 1:
        return 1

    low = 0
    high = 1 + (num/2)

    while low + 1 < high:
        mid = low + int(high-low)//2
        square = mid**2

        if square == num:
            return f'Square root of {num} is {mid}\n'
        elif square < num:
            low = mid
        else:
            high = mid

    return f'Nearest Square root of {num} is {low}\n'

print(sqrtFinder(16))
print(sqrtFinder(28))
print(sqrtFinder(36))
print(sqrtFinder(81))
print(sqrtFinder(50))
print(sqrtFinder(10))