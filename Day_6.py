#Day 6 : Find even & odd numbers in a list
print("\n---------Approach 1---------")
list1 = [9,8,7,6,5,4,3,2,1,0]
even1 = [i for i in list1 if i%2 == 0 ]
odd1 = [i for i in list1 if i%2 != 0 ]
print("Even numbers in the list:",even1)
print("Odd numbers in the list:",odd1)

print("\n---------Approach 2---------")
list2 = [20, 31, 52, 63, 74, 55, 86, 27, 98, 49]
even2 = list(filter(lambda l: l%2 == 0, list2))
odd2 = list(filter(lambda l: l%2 != 0, list2))
print("Even numbers in the list:",even2)
print("Odd numbers in the list:",odd2)

print("\n---------Approach 3---------")
list3 = [57,14,83,72,65,37,29,42,36]
even3, odd3 = [], []
for i in list3:
    if i%2 == 0:
        even3.append(i)
    else:
        odd3.append(i)
print("Even numbers in the list:",even3)
print("Odd numbers in the list:",odd3)