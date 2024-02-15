# Given five positive integers, find the minimum and maximum values that can be calculated by summing exactly four of the five integers. Then print the respective minimum and maximum values as a single line of two space-separated long integers.

# Example

# The minimum sum is  and the maximum sum is . The function prints

# 16 24
# Function Description

# Complete the miniMaxSum function in the editor below.

# miniMaxSum has the following parameter(s):

# arr: an array of  integers
# Print

# Print two space-separated integers on one line: the minimum sum and the maximum sum of  of  elements.

# Input Format

# A single line of five space-separated integers.

# Constraints
# 1 <= arr[i] <= 10^9

# Output Format

# Print two space-separated long integers denoting the respective minimum and maximum values that can be calculated by summing exactly four of the five integers. (The output can be greater than a 32 bit integer.)

def miniMaxSum(arr):
    
    array_min, array_max = arr.copy(), arr.copy()
    
    array_max.remove(min(array_max))
    array_min.remove(max(array_min))
    sum_max = sum(array_max)
    sum_min = sum(array_min)

    return print(sum_min, sum_max)

arr = list(map(int, input().rstrip().split()))

miniMaxSum(arr)