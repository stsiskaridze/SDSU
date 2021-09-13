import numpy as np

def merge(A, p, q, r):
    n1 = q - p + 1
    n2 = r - q
    L = [None]*(n1+1)
    R = [None]*(n2+1)
    for i in range(n1):
        L[i] = A[p + i]
    for j in range(n2):
        R[j] = A[q + 1 + j]
    L[n1] = np.inf
    R[n2] = np.inf
    i = 0
    j = 0
    for  k in range(p,r+1):
        if L[i] <= R[j]:
            A[k] = L[i]
            i = i + 1
        else:
            A[k] = R[j]
            j = j + 1

def mergeSort(A, p, r):
    if p < r:
        q = (p + r)//2
        mergeSort(A, p, q)
        mergeSort(A, q+1, r)
        merge(A, p, q, r)

A = [5, 4, 2, 7, 1, 3, 2, 6]
mergeSort(A, 0, len(A)-1)
print(A)