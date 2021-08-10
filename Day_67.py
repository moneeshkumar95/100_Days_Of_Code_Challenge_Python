print('Day 67: String compression\n')

def compress(st):
    dic = {}

    for i in st:
        dic.setdefault(i, 0)
        dic[i] += 1

    res = ''
    for j in dic:
        res += f'{j}{str(dic[j])}'

    return res

string = 'AAABCCCCDD'
print(f'Input: {string}\nOutput: {compress(string)}')

string2 = 'ZZxxxYYYzzz'
print(f'\nInput: {string2}\nOutput: {compress(string2)}')

