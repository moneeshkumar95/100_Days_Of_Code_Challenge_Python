print('\nDay 31: Insertion at the beginning in ordered dict')

print("\n-----------------Approach 1-----------------")
from collections import OrderedDict

dict = OrderedDict([(2, 'WISH IT'), (3, 'DO IT')])
print('Input:\n Orignial_Dict =',dict)
dict.update({1: 'DREAM IT'})
print(" Inserted Item = {1: 'DREAM IT'}")
dict.move_to_end(1, last=False)

print( 'Output:\n Final_Dict =',dict)

print("\n-----------------Approach 2-----------------")
dict1 = OrderedDict([(3, 'NEVER QUIT')])
dict2 = OrderedDict([(1, 'STAY HUMBLE'), (2, 'KEEP LEARNING')])

dict3 = OrderedDict(list(dict2.items()) + list(dict1.items()))

print( f'Input:\n Dict1 = {dict1}\n Dict2 = {dict2}  ')
print( f'Output:\n New_Dict = {dict3}')
