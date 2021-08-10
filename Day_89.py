print('Day 89\n')
import math

def calculateDivisors(A, B):
    N = A - B
    noOfDivisors = 0

    a = math.sqrt(N)
    for i in range(1, int(a + 1)):

        if N % i == 0:

            if i > B:
                noOfDivisors += 1

            if (N / i) != i and (N / i) > B:
                noOfDivisors += 1

    return noOfDivisors

def numberOfPossibleWaysUtil(A, B):
    if A == B:
        return -1

    if A < B:
        return 0

    noOfDivisors = 0
    noOfDivisors = calculateDivisors(A, B)

    return noOfDivisors

def numberOfPossibleWays(A, B):
    noOfSolutions = numberOfPossibleWaysUtil(A, B)

    if noOfSolutions == -1:
        print(f'Input: A={A} & B={B}\n'
              f'Output: X can take Infinitely many values'
              f'greater than {A}\n')

    else:
        print(f'Input: A={A} & B={B}\n'
              f'Output: X can take {noOfSolutions} values\n')


numberOfPossibleWays(21, 5)
numberOfPossibleWays(26, 2)











