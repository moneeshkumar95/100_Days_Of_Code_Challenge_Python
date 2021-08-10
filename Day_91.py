print('Day 91\n')

from collections import OrderedDict

def repeatingCharCheck(st, k):

    dict = OrderedDict.fromkeys(st, 0)

    for ch in st:
        dict[ch] += 1

    nonRepeatDict = [key for (key, value) in dict.items() if value == 1]

    if len(nonRepeatDict) < k:
        return 'Less than k non-repeating characters in given string'
    else:
        return nonRepeatDict[k-1]

print('------Input-----')
string = input('Please enter a string: ')
K = int(input('Please enter the k value: '))
print('\nOutput:', repeatingCharCheck(string, K))