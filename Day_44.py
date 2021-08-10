print('Day 44: Move negative number to the beginning\n')

def moveNeg(arr):

    j = 0
    for i in range(len(arr)):
        if (arr[i] < 0):
            temp = arr[i]
            arr[i] = arr[j]
            arr[j] = temp
            j = j + 1
    return arr

arr = [5,7,-2,1,-3,8,2,-4]
print('Input:',arr)
print('\nOutput:',moveNeg(arr))
