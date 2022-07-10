import numpy as np

name = input("Give me your name: ")
print(f"Your name is {name}")


def get_age(number):
    try:
        age = int(input(number))
        if age < 0:
            raise ValueError
        if age > 100:
            raise Exception
        return age

    except ValueError:
        print(f"Input must be a positive number!")
        return get_age(number)
    except Exception:
        print(f"You are older than The Hundred-Year-Old Man!")


# Enter input
user_age = get_age("Input your age: ")
year = 100 - user_age

print(
    f"You are now, {user_age}, years old \nThere should be {year} years to get 100 years old!"
)

