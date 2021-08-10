print('Day 21: Add,Subtract,Multiply and Divide two matrices')

import numpy as np

A = np.array([[0,1,2],[9,8,7]])
B = np.array([[6,5,4],[3,2,1]])

add = np.add(A,B)
sub = np.subtract(A,B)
mut = np.multiply(A,B)
div = np.divide(A,B)

print( f'Matrix A:\n{A}')
print( f'\nMatrix B:\n{B}')
print( f'\nMatrix A + B:\n{add}')
print( f'\nMatrix A - B:\n{sub}')
print( f'\nMatrix A * B:\n{mut}')
print( f'\nMatrix A / B:\n{div}')