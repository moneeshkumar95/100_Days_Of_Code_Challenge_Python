print('Day 58: Implementation of Merge Sort\n')

def mergeSort(arr):
    if len(arr) > 1:
        middle = len(arr)//2
        first_half = arr[:middle]
        second_half = arr[middle:]
        mergeSort(first_half)
        mergeSort(second_half)
        i,j,k = 0,0,0

        while i < len(first_half) and j < len(second_half):
            if first_half[i] < second_half[j]:
                arr[k] = first_half[i]
                i += 1
            else:
                arr[k] = second_half[j]
                j += 1
            k += 1
        while i < len(first_half):
            arr[k] = first_half[i]
            i += 1
            k += 1
        while j < len(second_half):
            arr[k] = second_half[j]
            j += 1
            k += 1
        print('Merging',arr)
        return arr

nums = [63,21,12,84,2,73,95,7,42,88,49]
print('\nOutput:',mergeSort(nums))