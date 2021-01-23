# Input: A sequence of n numbers A = [a1, a2, ..., an]
# Output: A sorted sequence B=[a1', ..., an'] in ascending order.

def findSmallest(A, key):
    min_index = key
    for i in range (key, len(A)):
        if A[i] < A[min_index]:
            min_index = i
    return min_index

def swap(A, i, j):
    tmp = A[i]
    A[i] = A[j]
    A[j] = tmp

A = [5, 2, 4, 6, 1, 3]

for key_index in range(len(A)):
    min_index = findSmallest(A, key_index)
    swap(A, min_index, key_index)

print(f"A sorted sequence is: {A}.")