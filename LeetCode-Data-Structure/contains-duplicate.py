# Given an integer array nums, return true if any value appears at least twice in the array, and return false if every element is distinct.

# Time Limit Exceeded
# O(n^2)
# class Solution:
#     i = 0
#     def containsDuplicate(self, nums: List[int]) -> bool:
#         for i in range(0,len(nums)):
#             for j in range(i+1,len(nums)):
#                 if nums[i] == nums[j]:
#                     return True

# Time complexity:
# O(n) - We iterate over the array once.

# Space complexity:
# O(n) - We use a hash set to store the elements.

from typing import List

# 549 ms
def containsDuplicate(nums: List[int]) -> bool:
    # Create an empty hash set
    cnt_set = set()
    # Iterate over the given list
    for num in nums:
        if num not in cnt_set:
            cnt_set.add(num)
        else:
            return True

nums = [1,1,1,3,3,4,3,2,4,2]
print(containsDuplicate(nums))