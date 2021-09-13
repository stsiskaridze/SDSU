import numpy as np 
  
def divide(A): 
    """ 
    Divide a given matrix A into four matricies. 
    Input: n x n matrix 
    Output: tuple containing four n/2 x n/2 matrices corresponding to A11, A12, A21, A22
    """
    m, n = A.shape 
    row, col = m//2, n//2
    A11 = A[:row, :col]
    A12 = A[:row, col:]
    A21 = A[row:, :col]
    A22 = A[row:, col:] 
    return A11, A12, A21, A22
  
def squareMatrixMultiplyRecursive(A, B): 
    """ 
    Computes matrix product by D&C approach, recursively. 
    Input: n x n matrix A and n x n marix Y 
    Output: n x n matrix, product of A and B 
    """
    # Base case when size of matrices is 1x1 
    if len(A) == 1: 
        return A * B 
  
    # Splitting the matrices into quadrants recursively.
    A11, A12, A21, A22 = divide(A) 
    B11, B12, B21, B22 = divide(B) 
      
    # Computing the values of the 4 quadrants of the final matrix c 
    C11 = squareMatrixMultiplyRecursive(A11, B11) + squareMatrixMultiplyRecursive (A12, B21)
    C12 = squareMatrixMultiplyRecursive(A11, B12) + squareMatrixMultiplyRecursive (A12, B22)
    C21 = squareMatrixMultiplyRecursive(A21, B11) + squareMatrixMultiplyRecursive (A22, B21)
    C22 = squareMatrixMultiplyRecursive(A21, B22) + squareMatrixMultiplyRecursive (A22, B22)
  
    # Combining the 4 quadrants into a single matrix by stacking horizontally and vertically. 
    C = np.vstack((np.hstack((C11, C12)), np.hstack((C21, C22))))  
  
    return C

#A = np.array([[1, 2], [3, 4]])
#B = np.array([[1, 2], [3, 4]])

A = np.array([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12], [13, 14, 15, 16]])
B = np.array([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12], [13, 14, 15, 16]])

C = squaxreMatrixMultiplyRecursive(A,B)
print(C)