print('Day 55: Implementation of Selection Sort\n')

def selectionSort(arr):

    for i in range(len(arr)-1,0,-1):
        k = 0

        for j in range(1, i+1):

            if arr[k] < arr[j]:
                k = j

        temp = arr[i]
        arr[i] = arr[k]
        arr[k] = temp

    return arr

num = [67,21,142,263,12,88,2]
print('Input:',num)
print('Output:',selectionSort(num))