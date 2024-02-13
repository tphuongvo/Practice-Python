import math
import os
import random
import re
import sys


def addDigit(len_digit, n, const):
    
    adding_zeros = n*pow(10,len_digit) + int(const)

    return adding_zeros

def numberAdding(n, k):
    number_temp = int(n)
    const = int(n)

    if (k == 1):
        sum_lst = list(map(int, str(number_temp)))
        # print(sum_lst)
    elif (k > 1):
        for _ in range(k-1):
            number = addDigit(len(str(n)),number_temp, const)
            number_temp = number
            # print(number_temp)
    
        sum_lst = list(map(int, str(number)))
    
    return sum(sum_lst)


def superDigit(n, k):

    sum_lst = numberAdding(n,k)
    # print(sum_lst)
    if len(str(sum_lst))==1:
        return sum_lst
    else:        
        return superDigit(n=sum_lst,k=1)
    

first_multiple_input = input().rstrip().split()

n = first_multiple_input[0]

k = int(first_multiple_input[1])

result = superDigit(n, k)
print(result)