print('Day 15: Matrix creation of n*n')

print("\n-------Approach 1-------")
n = int(input("Enter the n value: "))
print( f"\nCreated {n}*{n} matrix:")
matrix = [print(list(range(1 + n*i, 1 + n*(i+1)))) for i in range(n)]


print("\n-------Approach 2-------")
import itertools
n = int(input("Enter the n value: "))
value = itertools.count(n*n)
print( f"\nCreated {n}*{n} matrix:")
matrix2 = [print([next(value) for i in range(n)]) for i in range(n)]