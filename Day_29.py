print('\nDay 29: Check if the string contain the defined character using regex')

import re

def check(str, pattern):
    if re.search(pattern, str):
        print(f'\n{str} - Valid String')
    else:
        print(f'\n{str} - Invalid String')

pattern = re.compile('yourself$')

print('\nOutput:')

check('Believe in yourself',pattern)
check('self doubt', pattern)