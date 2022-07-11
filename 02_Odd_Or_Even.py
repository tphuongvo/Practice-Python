def check_number(number):
    try:
        num = int(input(number))
        if num < 0:
            raise ValueError
        return num

    except ValueError:
        print(f"Input must be a possitve number!")
        return check_number(number)


# Enter input
num = check_number(f"Enter your number to check: ")
check = check_number(f"Enter your number to divide by: ")

if check % num == 0:
    print("Your Check divides evenly into Num.")
else:
    print("Your Check does not devides evently into your Num.")

