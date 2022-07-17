import numpy as np


class filter:
    def __init__(self, a: list):
        self.a = a

    def print_out(self):
        """The first requirement is printing out all 
        the elements of the list that are less than 5"""

        print(f"The first requirement: One by one")
        for x in self.a:
            if x < 5:
                print(x)

    def make_list(self):
        """Instead of printing the elements one by one,
        make a new list that has all the elements less
        than 5 from this list in it and print out this new list"""

        new_list = []
        print(f"The second requirement: New list")
        for x in self.a:
            if x < 5:
                new_list.append(x)
        print(new_list)

    def get_number(self):
        """Ask the user for a number and return a list that contains
        only elements from the original list a that are smaller than
        that number given by the user"""

        def input_number(number):
            try:
                input_num = int(input(number))
                return input_num
            except Exception:
                print(f"input must be a number!")
                return input_number(number)

        print(f"The third requirement: ask for a reference number")
        ref_num = input_number("Input a number: ")
        new_list = []
        for x in self.a:
            if x < ref_num:
                new_list.append(x)
        print(new_list)


list = filter([1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89])
list.print_out()
list.make_list()
list.get_number()
