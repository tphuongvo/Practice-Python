"""
Algorithms, Design and Analysis, Part I.
Programming Assignment 2:

Count inversions using Merge Sort.
"""

# Running time: T(n) = O(n log n)
import math


def merge_inversion(left, right):
    res_arr, inv_count = [], 0
    while len(left) > 0 or len(right) > 0:
        i, j = 0, 0
        if len(left) > 0 and len(right) > 0:
            if left[i] < right[j]:
                res_arr.append(left[i])
                i += 1
                left = left[i:]
            else:
                res_arr.append(right[j])
                j += 1
                right = right[j:]
                inv_count += len(left)
        elif len(left) > 0:
            res_arr.append(left[i])
            i += 1
            left = left[i:]
        elif len(right) > 0:
            res_arr.append(right[j])
            j += 1
            right = right[j:]

    return res_arr, inv_count


def merge_count_inversion(lst):
    size = len(lst)
    if len(lst) <= 1:
        return lst, 0
    mid = math.ceil(size // 2)  # no matter when choosing ceil or floor
    left, a = merge_count_inversion(lst[:mid])
    right, b = merge_count_inversion(lst[mid:])
    result, c = merge_inversion(left, right)
    return result, (a + b + c)


# list = [1, 3, 5, 2, 4, 6]
# print(merge_count_inversion(list))
with open("ItegerArray.txt", "r") as f:
    results = merge_count_inversion([int(i) for i in f])

print(results[1])  # 2407905288
