print('Day 39: Find kth column of a matrix\n')

def find(mat, k):
    kth_column = [row[k-1] for row in mat]
    return kth_column

matrix = [
            [11,12,13,14,15],
            [21,22,23,24,25],
            [31,32,33,34,35],
            [41,42,43,44,45],
            [51,52,53,54,55],
            [61,62,63,64,65]
]
k = int(input('Enter the K value: '))
print(f'\nColumn {k} of a matrix is {find(matrix, k)}')
