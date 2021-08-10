print('Day 54: Implementation of Bubble Sort\n')

def bubbleSort(num):

    for i in range(len(num)-1,0,-1):

        for j in range(i):

            if num[j] > num[j+1]:
                temp = num[j]
                num[j] = num[j+1]
                num[j+1] = temp
    return num

nums = [30,64,78,95,14,21,47]
print('Input:',nums)
print('Output:',bubbleSort(nums))
