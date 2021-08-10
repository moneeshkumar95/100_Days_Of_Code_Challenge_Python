print('Day 59: Program to print diamond shape\n')

def shapeCreater(num):
    n = 0
    for i in range(1, num + 1):

        for j in range(1, (num - i) + 1):
            print(end=' ')

        while n != (2 * i - 1):
            print('*', end='')
            n += 1
        n = 0

        print()

    k, n = 1, 1
    for i in range(1, num):

        for j in range(1, k+1):
            print(end=' ')
        k += 1

        while n <= (2 * (num - i) -1):
            print('*', end='')
            n += 1
        n = 1

        print()

row = int(input("Enter the diamond row: "))
shapeCreater(row)