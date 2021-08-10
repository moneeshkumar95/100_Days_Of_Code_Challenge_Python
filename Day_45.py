print('Day 45: Check if string contains unique characters\n')

def check(str):

    if len(str) > 256:
        return False

    char_set = [False] * 128

    for i in range(0, len(str)):
        val = ord(str[i])
        if char_set[val]:
            return f'{str} is not Unique'
        char_set[val] = f'{str} is Unique'
    return f'{str} is Unique'

string = input("Enter a string: ")
print('\nOutput:',check(string))

string = input("\nEnter a string: ")
print('\nOutput:',check(string))