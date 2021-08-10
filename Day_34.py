print('Day 34: Convert snake case to pascal case')

print("\n-------------Approach 1-------------")
import string

str1 = 'change_is_never_easy_but_always_possible'
converted_str1 = string.capwords(str1.replace('_',' ')).replace(' ','')
print( 'Input:',str1)
print('Output:',converted_str1)

print("\n-------------Approach 2-------------")
str2 = 'you_never_fail_until_you_stop_trying'
converted_str2 = str2.title().replace('_','')
print( 'Input:',str2)
print('Output:',converted_str2)