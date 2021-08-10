print("""Day 71: Difference between 2nd largest 
        and 2nd smallest number""")

print("\n--------Approach 1-------")
def checkDiff1(list1):
    largest = list1[0]
    lowest = list1[0]
    largest2 = None
    lowest2 = None

    for item in list1[1:]:
        if item > largest:
            largest2 = largest
            largest = item
        elif largest2 == None or largest2 < item:
            largest2 = item
        if item < lowest:
            lowest2 = lowest
            lowest = item
        elif lowest2 == None or lowest2 > item:
            lowest2 = item

    print('2nd largest number is', largest2)
    print('2nd lowest number is', lowest2)
    print('\nDifference is', largest2 - lowest2)

l1 = [28,67,12,88,92,36,54]
checkDiff1(l1)


print("\n--------Approach 2-------")
def checkDiff2(list2):
    list2.sort()

    print('2nd largest number is', list2[-2])
    print('2nd lowest number is', list2[1])
    print('\nDifference is', list2[-2] - list2[1])

l2 = [74,19,61,59,32,11,46]
checkDiff2(l2)



















