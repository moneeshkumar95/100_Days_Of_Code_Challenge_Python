print('Day 68: Recursion Problems')

print("\n--------Approach 1-------")
def rec_sum1(n):
    if n > 1:
        n += rec_sum1(n-1)
    return n

print(rec_sum1(10))

print("\n--------Approach 2-------")
def rec_sum2(n):
    return n + rec_sum2(n-1) if n > 1 else n

print(rec_sum2(15))

print("\n--------Approach 3-------")
def rec_sum3(n):
    if n == 0:
        return 0
    else:
        return n + rec_sum3(n-1)

print(rec_sum3(5))
