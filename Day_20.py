print('Day 20: Cloning a list')

print("\n------------Approach 1------------")
lis1 = [2,4,6,8,10,12]
lis2 = list(lis1)
print( f'Original List: {lis1}\nCloned List: {lis2}')

print("\n------------Approach 2------------")
lis1 = [3,6,9,12,15,18]
lis2 = [i for i in lis1]
print( f'Original List: {lis1}\nCloned List: {lis2}')

print("\n------------Approach 3------------")
lis1 = [4,8,12,16,20,24]
lis2 = lis1[:]
print( f'Original List: {lis1}\nCloned List: {lis2}')

print("\n------------Approach 4------------")
lis1 = [5,10,15,20,25,30]
lis2 = lis1.copy()
print( f'Original List: {lis1}\nCloned List: {lis2}')