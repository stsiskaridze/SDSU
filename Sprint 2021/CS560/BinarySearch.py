# Input: An ordered sequence of n numbers A = [a1, a2, ..., an] and a value v
# Output: An index i such that v = A[i] or the special value None if v does not appear in A.

A = [0, 1, 2, 3, 4, 5, 6, 7]
v = 3

index = None
left = 0
right = len(A)-1
while left <= right and index is None: 
    middle = left + (right - left) // 2
    if A[middle] == v: 
        index = middle
    elif A[middle] < v:
        left = middle + 1
    else: 
        right = middle - 1
 
if index is not None: 
    print (f"The item has been found on the index {index} ") 
else: 
    print ("The element could not be found!") 