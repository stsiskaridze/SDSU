import numpy as np

def findMaxCrossingSubarray(A, low, mid, high):
    left_sum = -np.inf
    sum = 0
    max_left = mid
    for i in range(mid, low, -1):
        sum = sum + A[i]
        if sum > left_sum:
            left_sum = sum
            max_left = i
    right_sum = -np.inf
    sum = 0
    max_right = mid + 1
    for j in range(mid + 1, high):
        sum = sum + A[j]
        if sum > right_sum:
            right_sum = sum
            max_right = j            
    return max_left, max_right, left_sum + right_sum       

def findMaximumSubarray(A, low, high):
    if high == low:
        return low, high, A[low]
    else:
        mid = (low + high)//2
        left_low,  left_high,  left_sum  = findMaximumSubarray(A, low,    mid )
        right_low, right_high, right_sum = findMaximumSubarray(A, mid+1 , high)
        cross_low, cross_high, cross_sum = findMaxCrossingSubarray(A, low, mid, high)
    if left_sum >= right_sum and left_sum >= cross_sum:
        return left_low, left_high, left_sum
    if right_sum >= left_sum and right_sum >= cross_sum:
        return right_low, right_high, right_sum
    if cross_sum >= left_sum and cross_sum >= right_sum:
        return cross_low, cross_high, cross_sum

#B = [100, 113, 110, 85, 105, 102, 86, 63, 81, 101, 94, 106, 101, 79, 94, 90, 97]
#A = [B[i+1]-B[i] for i in range(len(B)-1)]
A = [3, -1, 4, -1, 5, -9, -2, -6, 5, -3, 5, -9]
#print(f"B = {B}")
print(f"A = {A}")

low, high, sum = findMaximumSubarray(A, 0, len(A)-1)
print(f" Low index = {low}")
print(f" High index = {high}")
print(f" Sum  = {sum}")