print('Day 28: Check if the email id is valid or not')

import re
regex = '(\w|\.\-)+[@](\w|\.\-)+[.]\w{2,3}$'
def check(email):
    if re.search(regex,email):
        print(email,'is a valid Email')
    else:
        print(email, 'is not a valid Email')
email1 = input("\nEnter the 1st Email: ")
email2 = input("Enter the 2nd Email: ")
print('\nOutput:')
check(email1)
check(email2)
# ^ - starts with
# $ - ends with
# \w = any character(a-z, 0-9,...)
# / - either or
# \. - includes .
# \- - includes -
# (-) - group
# [] - set of characters
# \w{2,3} - 2 or 3 occurrences of \w