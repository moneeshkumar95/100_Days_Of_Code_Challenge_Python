print('Day 47: Check if two lists have atleast one element in common\n')

def check(l1, l2):
    l1 = set(l1)
    l2 = set(l2)

    if len(l1.intersection(l2)) > 0:
        return 'It has one element in common'
    return 'It has no common element'

list1 = [0,9,8,7,6]
list2 = [5,4,3,2,1]
print('Input:',list1,list2)
print('Output:',check(list1, list2))

list3 = ['a','b','c','d']
list4 = ['d','e','f','g']
print('\nInput:',list3,list4)
print('Output:',check(list3, list4))