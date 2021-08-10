print('Day 56: Implementation of Insertion Sort\n')

def insertionSort(num):

    for i in range(1, len(num)):

        currentvalue = num[i]
        position = i

        while position > 0 and num[position - 1] > currentvalue:

            num[position] = num[position - 1]
            position = position -1

        num[position] = currentvalue

    return num

nums = [34,16,22,-7,12,-10,5,-3]
print('Input:',nums)
print('Output:',insertionSort(nums))