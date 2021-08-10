print('Day 70: Implementation of fibonacci series')

print("\n--------Approach 1-------")
def fib_iter(n):
    a, b = 0, 1

    for i in range(n):
        a, b = b, a+b

    return a

print('Output:',fib_iter(6))



print("\n--------Approach 2-------")
def fib_rec(n):

    if n == 0 or n == 1:
        return n
    return fib_rec(n-1) + fib_rec(n-2)

print('Output:',fib_rec(12))




print("\n--------Approach 3-------")
n = 10
cache = [None]*(n+1)

def fib_dyn(n):

    if n == 0 or n == 1:
        return n

    if cache[n] != None:
        return cache[n]

    cache[n] = fib_dyn(n-1) + fib_dyn(n-2)

    return cache[n]

print('Output:',fib_dyn(9))









