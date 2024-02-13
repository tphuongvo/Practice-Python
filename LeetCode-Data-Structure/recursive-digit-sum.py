# We define super digit of an integer  using the following rules:

# Given an integer, we need to find the super digit of the integer.

# If  has only  digit, then its super digit is .
# Otherwise, the super digit of  is equal to the super digit of the sum of the digits of .
# For example, the super digit of  will be calculated as:

# 	super_digit(9875)   9+8+7+5 = 29 
# 	super_digit(29) 	2 + 9 = 11
# 	super_digit(11)		1 + 1 = 2
# 	super_digit(2)		= 2

def addDigit(len_digit, n, const):
    
    adding_zeros = n*pow(10,len_digit) + int(const)

    return adding_zeros

def numberAdding(n, k):

    number_temp = int(n)
    const = int(n)

    if (k == 1):
        sum_lst = list(map(int, str(number_temp)))
    elif (k > 1):
        for _ in range(k-1):
            number = addDigit(len(str(n)),number_temp, const)
            number_temp = number
    
        sum_lst = list(map(int, str(number)))
    
    return sum(sum_lst)


def superDigit_2(n, k):

    sum_lst = numberAdding(n,k)

    if len(str(sum_lst))==1:
        return sum_lst
    else:        
        return superDigit_2(n=sum_lst,k=1)


## Solution
def superDigit(n, k):

    sum_result = str(sum([int(number) for number in n])*k)

    if len(sum_result) != 1:
        return superDigit(sum_result,1)
    else:
        return sum_result


first_multiple_input = input().rstrip().split()

n = first_multiple_input[0]

k = int(first_multiple_input[1])

print(superDigit(n, k))
print(superDigit_2(n, k))