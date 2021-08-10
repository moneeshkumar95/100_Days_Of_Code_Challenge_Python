print('Day 53: Implementation of Recursive Binary Search\n')

def recBinSearch(arr, n):

    if len(arr) == 0:
        return False
    else:
        mid = len(arr)//2

        if n == arr[mid]:
            return True
        elif n < arr[mid]:
            return recBinSearch(arr[:mid], n)
        return recBinSearch(arr[mid+1:], n)

arr = [1,2,3,4,5,6,7,8,9]
print(recBinSearch(arr, 14))
print(recBinSearch(arr, 7))