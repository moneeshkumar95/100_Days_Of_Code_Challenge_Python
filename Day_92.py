print('Day 92\n')

def check(s, k):
    result = ''

    while True:
        temp = 0

        for i in s[:k]:
            temp += int(i)

        result += str(temp)

        s = s[k:]
        k -= 1

        if k == 0:
            k = 3

        if s == '':
            break

    return result

S = input('Enter the S value: ')
K = int(input('Enter the K value: '))
print('\nOutput:', check(S, K))