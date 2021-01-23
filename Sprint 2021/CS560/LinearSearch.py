# Input: A sequence of n numbers A = [a1, a2, ..., an] and a value v
# Output: An index i such that v = A[i] or the special value None if v does not appear in A.

A = [5, 2, 4, 6, 1, 3]
v = 9

i = 0
index = None
isNull = True
while i < len(A) and isNull:
    if v == A[i]:
        isNull = False
        index = i
    i = i+1

if isNull == False:    
    print(f"Item with value {v} has been found. Item index =  {index}. A[index] = {A[index]}")
else:
    print("Item has not been found!")