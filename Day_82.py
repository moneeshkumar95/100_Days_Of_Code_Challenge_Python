print('Day 82\n')

from random import randint

def dice7():
    return randint(1,7)

def convert7to5():
    roll = 7

    while roll > 5:

        roll = dice7()
        print('dice7() produced a roll of',roll)

    return f'Your final returned roll is {roll}'

print(convert7to5())