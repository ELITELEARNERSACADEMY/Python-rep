#  Python Program to Print an Identity Matrix
import numpy as np
def identy_matrix(n):
                print(np.identity(n))
                
                
print('Print an Identity Matrix')

try:
        n = int(input('Enter the size of the matrice'))
except:
         print('Error, please enter an integer value for the size')
         n = int(input('Enter the size of the matrice'))

identy_matrix(n)
