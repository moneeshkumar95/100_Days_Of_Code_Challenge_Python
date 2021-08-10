print('Day 88\n')

def hasConsecutiveZeroes(n, k):
    z = tok(n, k)
    if check(z):
        print("Yes")
    else:
        print("No")

def tok(n, k):
    w = 1
    s = 0
    while n != 0:
        r = n % k
        n = n // k
        s = r * w + s
        w *= 10
    return s

def check(n):
    fl = False
    while n != 0:
        r = n % 10
        n = n // 10

        if fl == True and r == 0:
            return False
        if r > 0:
            fl = False
            continue
        fl = True
    return True

hasConsecutiveZeroes(15, 8)
hasConsecutiveZeroes(4, 2)
