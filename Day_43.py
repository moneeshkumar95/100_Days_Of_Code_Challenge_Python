print('Day 43: Find the Unique elements in the list')

print("\n-------------Approach 1-------------")
def check1(lst):
    uniq_elem1 = []
    for i in lst:
        if i not in uniq_elem1:
            uniq_elem1.append(i)
    return uniq_elem1
list1 = ['i3','i7','i5','i3','i9','i7','i3']
print('Unique:',check1(list1))

print("\n-------------Approach 2-------------")
def check2(lst):
    uniq_elem2 = set(lst)
    return list(uniq_elem2)
list2 = [40,30,50,10,20,40,30,20,10]
print('Unique:',check2(list2))

print("\n-------------Approach 3-------------")
from collections import Counter
def check3(lst):
    return list(Counter(lst))
list3 = ['HP','Dell','HP','Acer','Asus','Dell']
print('Unique:',check3(list3))

print("\n-------------Approach 4-------------")
from numpy import unique
def check4(lst):
    return list(unique(lst))
list4 = [40,30,50,10,20,40,30,20,10]
print('Unique:',check4(list4))