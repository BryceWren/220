"""
Bryce Wren: Lab 12
"""


def find_and_remove_first(the_list, value):
    i = 0
    found = False
    while i <= len(the_list) - 1 and not found:
        if value == the_list[i]:
            the_list.pop(i)
            the_list.insert(i, "Bryce")
            found = True
        else:
            i += 1


def good_input():
    user_input = eval(input("enter a number in range of 1-10"))
    if (user_input >= 1) and (user_input <= 10):
        print("good input")
    elif user_input < 1:
        print("too low of a number")
        good_input()
    elif user_input > 10:
        print("too high of a number")
        good_input()

def num_digits():
    my_list = []
    user_input = eval(input("enter a positive integer"))
    while user_input <= 0:
        if user_input > 0:
            my_list.append(user_input)


num_digits()

def hi_lo_game():
    pass

