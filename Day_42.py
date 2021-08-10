print('Day 42: Group similar elements in a list')

print("\n-------------Approach 1-------------")
import itertools

list_1 = ['Tea','Coffee','Milk','Juice','Coffee','Soda']
result1 = [list(j) for i,j in itertools.groupby(sorted(list_1))]

print('Input:',list_1)
print('\nOutput:',result1)

print("\n-------------Approach 2-------------")
from collections import Counter

list_2 = [6,2,7,6,9,4,2,8,1]
result2 = [[i]*j for i,j in Counter(list_2).items()]

print('Input:',list_2)
print('\nOutput:',sorted(result2))