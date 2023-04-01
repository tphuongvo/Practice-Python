# Given an integer array nums, find the subarray with the largest sum, and return its sum.

# Time Limit Exceeded for Brute Force Approach

# class Solution:
#     def maxSubArray(self, nums: List[int]) -> int:
#         sum_ = -np.inf
#         front,end = 0,0
#         if len(nums) == 1:
#             sum_ = nums[0]
#         else:
#             for j in range(0, len(nums)+1):
#                 for i in range(j, len(nums)):
#                     sum_lst = np.sum(nums[j:i+1])
#                     if round(sum_,1) < sum_lst:
#                         sum_ = sum_lst
#                         front = j
#                         end = i
#         return sum_

# Kadane's Algo
# Time Complexity: O(n)
# Runtime 718 ms

from typing import List

def maxSubArray(nums: List[int]) -> int:

    length_list = len(nums)
    global_max, local_max  =  float('-inf'), 0

    # loop over the array and find the maximum value of each subarray: 
    #  maxSum[i] = max(A[i], A[i] + maxSum[i-1])
    for indx in range(length_list):
        local_max += nums[indx]
        local_max = max(nums[indx], local_max)

        # replace the global max by the local one
        if local_max > global_max:
            global_max = local_max
        
    return global_max


nums = [-2,1,-3,4,-1,2,1,-5,4]
print(maxSubArray(nums))