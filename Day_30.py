print('''\nDay 30: Count the total number of uppercase, lowercase,
        numeric & special characters in a string''')

import re

print("\n-----------------Input-----------------")
string1 = input("Enter a string: ")

uppercase_chars = re.findall(r'[A-Z]', string1)
lowercase_chars = re.findall(r'[a-z]', string1)
numeric_chars = re.findall(r'[0-9]', string1)
special_chars = re.findall(r'[%+=-]', string1)

print("\n-----------------Output-----------------")
print('Total number of uppercase characters is',len(uppercase_chars))
print('Total number of lowercase characters is',len(lowercase_chars))
print('Total number of numeric characters is',len(numeric_chars))
print('Total number of special characters is',len(special_chars))
