"""
So: what's the product of the following two 64-digit numbers?
3141592653589793238462643383279502884197169399375105820974944592

2718281828459045235360287471352662497757247093699959574966967627

You can implement the grade-school algorithm if you want, but to get the most out of 
the assignment you'll want to implement recursive integer multiplication and/or Karatsuba's algorithm.
"""

import math


def input_number(number):
    try:
        input_num = str(input(number))
        return input_num
    except Exception:
        print(f"input integers")
        return input_number(number)


def karatsuba(x, y):
    len1, len2 = len(x), len(y)

    if len1 == 1 or len2 == 1:
        return str(int(x) * int(y))

    # determine the mid point
    size = min(len1, len2)
    mid = math.floor(size // 2)

    # Left and Right after splitting
    left_x = x[:mid]
    right_x = x[mid:]
    left_y = y[:mid]
    right_y = y[mid:]

    # recursively calls
    all_left = int(karatsuba(left_x, left_y))  # ac
    all_right = int(karatsuba(right_x, right_y))  # bd
    cross = int(
        karatsuba(str(int(left_x) + int(right_x)), str(int(left_y) + int(right_y)))
    )
    sum = cross - all_right - all_left  # ad + bc

    result = 10 ** (mid * 2) * all_left + 10 ** mid * sum + all_right
    return str(result)


x = input_number("Input x: ")
y = input_number("Input y: ")
print(karatsuba(x, y))

