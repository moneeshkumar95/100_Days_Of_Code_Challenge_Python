print('Day 99\n')

def factorial(n):
    res = 1

    for i in range(1, n + 1):
        res *= i
    return res

def binomialCoeff(n, k):
    res = 1

    if (k > n - k):
        k = n - k

    for i in range(k):
        res *= (n - i)
        res //= (i + 1)

    return res

def catalan(n):

    c = binomialCoeff(2 * n, n)

    return c // (n + 1)

def countBST(n):

    count = catalan(n)

    return count

def countBT(n):

    count = catalan(n)

    return count * factorial(n)



n = int(input('Enter the n value: '))

count1 = countBST(n)
count2 = countBT(n)

print(f'Total No. of possible binary '
      f'search trees with {n} nodes is {count1}')

print(f'Total No. of possible binary'
      f'trees with {n} nodes is {count2}')















