print('Day 65: Find the missing elements b/w two arrays\n')

arr1 = [9,8,7,6,5,3,2,1]
arr2 = [6,2,1,7,3,8,9]

print("\n--------Approach 1-------")
def check1(ar1,ar2):
    ar1.sort()
    ar2.sort()

    for num1, num2 in zip(ar1,ar2):
        if num1 != num2:
            return num1
    return ar1[-1]
print("Missing Element is",check1(arr1,arr2))

print("\n--------Approach 2-------")
def check2(ar1,ar2):
    result = 0

    for num in ar1+ar2:
        result ^= num
    return result
print("Missing Element is",check2(arr1,arr2))

print("\n--------Approach 3-------")
from collections import defaultdict
def check3(ar1,ar2):
    d = defaultdict(int)

    for num in ar2:
        d[num] += 1

    for num in ar1:
        if d[num] == 0:
            return num
        else:
            d[num] -= 1

print("Missing Element is",check3(arr1,arr2))