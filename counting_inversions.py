"""
Algorithms, Design and Analysis, Part I.
Programming Assignment 2:

Count inversions using Merge Sort.
"""

# Running time: T(n) = O(n log n)
import math


def merge_count_inversion(left, right):
    result_lst, inv_count = [], 0
    while len(left) > 0 or len(right) > 0:
        i, j = 0, 0
        if len(left) > 0 and len(right) > 0:
            if left[i] < right[j]:
                result_lst.append(left[i])
                i += 1
                left = left[i:]
            else:
                result_lst.append(right[j])
                j += 1
                right = right[j:]
                inv_count += len(left)
        elif len(left) > 0:
            result_lst.append(left[i])
            i += 1
            left = left[i:]
        elif len(right) > 0:
            result_lst.append(right[j])
            j += 1
            right = right[j:]

    return result_lst, inv_count


def split(lst):
    size = len(lst)
    if len(lst) <= 1:
        return lst, 0
    mid = math.ceil(size // 2)  # no matter when choosing ceil or floor
    left, a = split(lst[:mid])
    right, b = split(lst[mid:])
    result, c = merge_count_inversion(left, right)
    return result, (a + b + c)


def merge_sort_inversion_counting(file):
    with open(file, "r") as f:
        results = split([int(i) for i in f])
    return results[1]


# list = [1, 3, 5, 2, 4, 6]
# print(merge_count_inversion(list))
file = "ItegerArray.txt"
print(merge_sort_inversion_counting(file))  # 2407905288
