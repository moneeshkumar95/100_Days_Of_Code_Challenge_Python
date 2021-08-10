print('Day 87\n')

stack = []
top = -1

def push(ele):
    global top
    top += 1
    stack[top] = ele

def pop():
    global top
    ele = stack[top]
    top -= 1
    return ele

def isPalindrome(string):
    global stack
    length = len(string)

    stack = ['0'] * (length + 1)

    mid = length // 2
    i = 0
    while i < mid:
        push(string[i])
        i += 1

    if length % 2 != 0:
        i += 1

    while i < length:
        ele = pop()

        if ele != string[i]:
            return f'{string} is not a palindrome'
        i += 1
    return f'{string} is a palindrome'


print(isPalindrome('morning'))
print(isPalindrome('noon'))
print(isPalindrome('add'))
print(isPalindrome('pop'))