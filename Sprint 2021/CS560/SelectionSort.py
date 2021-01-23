# Input: A sequence of n numbers A = [a1, a2, ..., an]
# Output: A sorted sequence B=[a1', ..., an'] in ascending order.

A = [5, 2, 4, 6, 1, 3]
B = []

def findSmallest(A):
    key = A[0] 
    key_index = 0 
    for i in range(1, len(A)):
        if A[i] < key:
            key = A[i]
            key_index = i
    return key_index

for i in range(len(A)):
    key_index = findSmallest(A)
    B.append(A.pop(key_index))

print(f"A sorted sequence is: {B}.")