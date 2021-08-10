print('Day 19: Adding all values in dictionary')

print("\n------------Approach 1------------")
dict = {'a': 52, 'b': 74, 'c': 36, 'd': 87}
result = 0
for i in dict:
    result += dict[i]
print( f'Dictionary: {dict}\nThe sum is {result}')

print("\n------------Approach 2------------")
def add(d):
    result2 = 0
    for i in d.values():
        result2 += i
    return result2
dict = {'m': 14, 'n': 196, 'o': 81, 'p': 245}
print( f'Dictionary: {dict}\nThe sum is {add(dict)}')

print("\n------------Approach 3------------")
dict = {'w': 3048, 'x': 1693, 'y': 8704, 'z': 777}
print( f'Dictionary: {dict}\nThe sum is {sum(dict.values())}')