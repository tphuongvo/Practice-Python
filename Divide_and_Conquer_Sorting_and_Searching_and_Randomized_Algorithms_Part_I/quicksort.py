"""
Algorithms, Design and Analysis, Part I.
Programming Assignment 3:

Use Quicksort to count the number of comparisons.
The running time depends on which elements are chosen as pivots:
Case 1: The first element of the array as the pivot element
Case 2: The last element of the array as the pivot element
Case 3: the median element of the array as the pivot element
"""

import math

com_count = 0
# pivot_position = "first"
# pivot_position = "last"
pivot_position = "median"


def swap(lst, i, j):
    temp = lst[i]
    lst[i] = lst[j]
    lst[j] = temp


def median_of_three(lst):
    mid = 0
    if len(lst) % 2 == 0:
        mid = math.ceil(len(lst) // 2)
        ordset = [lst[0], lst[mid - 1], lst[-1]]
    else:
        mid = math.ceil(len(lst) // 2)
        ordset = [lst[0], lst[mid], lst[-1]]
    ordset.sort()
    return lst.index(ordset[1])


def pivot_and_search(lst):
    global pivot_position

    pivot_index = 0
    pivot = lst[pivot_index]
    stored_index = 1
    for i in range(1, len(lst)):
        if lst[i] < pivot or lst[i] == pivot:
            swap(lst, i, stored_index)
            stored_index += 1

    # Swap pivot with Array[increment]
    swap(lst, pivot_index, stored_index - 1)
    # lst[0], lst[stored_index - 1] = lst[stored_index - 1], lst[0]
    return (
        stored_index - 1
    )  # swap pivot with the last element -> pivot in sorted position


def quicksort(lst):
    global com_count, pivot_position
    if len(lst) <= 1:
        return lst
    com_count += len(lst) - 1
    if pivot_position == "first":
        pass
    elif pivot_position == "last":
        swap(lst, 0, len(lst) - 1)
    else:
        pivot_index = median_of_three(lst)
        pivot = lst[pivot_index]
        swap(lst, 0, pivot_index)

    pivot = pivot_and_search(lst)
    results = quicksort(lst[:pivot]) + [lst[pivot]] + quicksort(lst[pivot + 1 :])
    return results


def quick_sort_comparision_counting(file):
    with open(file, "r") as f:
        results = quicksort([int(i) for i in f])
    return results[1]


# lst1 = [5, 18, 6, 12, 30, 7, 35]
# print(quicksort(lst1))

file = "Quick_sort.txt"
print(quick_sort_comparision_counting(file))
print(com_count)
