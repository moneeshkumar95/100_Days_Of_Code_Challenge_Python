print('Day 64: Given an integer array, output all unique pairs that '
      'sum up to a specific value k\n')

def check(arr, k):
    if len(arr) < 2:
        return

    seen = set()
    output = set()

    for num in arr:
        target = k - num

        if target not in seen:
            seen.add(num)
        else:
            output.add((min(num,target), max(num,target)))

    return '\n '.join(map(str, list(output)))

print('Output 1:\n',check([3,2,2,1,0], 4))
print('\nOutput 2:\n',check([3,4,-2,14,5,9,12,-4,10,15,0,12,6,7], 10))
print('\nOutput 3:\n',check([10,2,7,5,14,8,1,9], 15))