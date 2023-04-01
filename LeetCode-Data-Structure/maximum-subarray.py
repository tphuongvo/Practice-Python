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