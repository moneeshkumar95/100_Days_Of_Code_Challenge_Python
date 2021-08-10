print('Day 72: Find the maximum occurring character')

print("\n--------Approach 1-------")
s = 'without risk there is no story'
freq = {}
for i in s:
    if i != ' ':
        if i in freq:
            freq[i] += 1
        else:
            freq[i] = 1

result = max(freq, key=freq.get)
print(f'Input: {s}\nOutput: {result}')


print("\n--------Approach 2-------")
from collections import Counter

s = 'you never fail until you stop trying'

res = Counter(s.replace(' ',''))
res = max(res, key=res.get)

print(f'Input: {s}\nOutput: {res}')
