print('Day 16: Reverse the given list')

print("\n------------Approach 1------------")
List1 = [9,8,7,6,5,4,2,1]
print('Original List:',List1)
print('Reversed List:',List1[::-1])

print("\n------------Approach 2------------")
List2 = [11,22,33,44,55,66]
print('Original List:',List2)
List2.reverse()
print('Reversed List:',List2)

print("\n------------Approach 3------------")
def rev(lst):
    print('Reversed List:',[i for i in lst])

List3 = [5,10,15,25,30,35]
print('Original List:',List3)
rev(reversed(List3))