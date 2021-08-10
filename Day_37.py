print('Day 37: Program for bubble sort')

print("\n-------------Bubble Sort-------------")

def bubbleSort(ar):
    l = len(ar)

    for i in range(l-1):

        for j in range(l-i-1):
            if ar[j] > ar[j+1]:
                ar[j+1], ar[j] = ar[j], ar[j+1]

arr = [82,17,93,54,26,73]
print('Before Bubble Sort:',arr)
bubbleSort(arr)
print('\nAfter Bubble Sort:',arr)
