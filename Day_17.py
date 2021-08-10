print('Day 17: Merging two dictionaries')

print("\n------------Approach 1------------")
dict1 = {'Python': 3.9, 'Django': 3.2}
dict2 = {'PostgreSQL': 13.3,'Mysql': 8.0}
print('Dict1:',dict1)
print('Dict2:',dict2)
dict1.update(dict2)
print('\nMerged:',dict1)

print("\n------------Approach 2------------")
dict1 = {'HTML': 5, 'CSS': 3}
dict2 = {'Javascript': 6,'Bootstrap': 5}
result = {**dict1, **dict2}
print('Dict1:',dict1)
print('Dict2:',dict2)
print('\nMerged:',result)