"""
Name: <Bryce Wren>
<ProgramName>.py

Problem: <Brief, one or two sentence description of the problem that this program solves, in your own words.>

Certification of Authenticity:
I certify that this assignment is entirely my own work
I certify that this assignment is entirely my own work.
"""


def calc_rec_area():
    length = eval(input("Enter the length: "))
    width = eval(input("Enter the width: "))
    area = length * width
    print("Area =", area)


def calc_volume():
    length = eval(input('Enter the length'))
    width = eval(input('Enter the width'))
    height = eval(input('Enter the height'))
    volume = length * width * height
    print("Volume", volume)


def shooting_percentage():
    total_shots = (eval(input("Enter the player's total shots:")))
    shots_made = (eval(input("Enter how many shots the player made:")))
    shot_percentage = shots_made / total_shots * 100
    print("Shooting Percentage:", shot_percentage, "%")


def coffee():
    coffee_cost = 10.50
    shipping_cost = .86
    fixed_cost = 1.50
    product = eval(input("How many pounds of coffee would you like?"))
    total = product * coffee_cost + shipping_cost * 2 + fixed_cost
    print("You're total is:", total)




def kilometers_to_miles():
    user = eval(input("How many Kilometers did you travel"))
    kilometer = 1.61
    miles_traveled = user / kilometer
    print("That's", miles_traveled, "miles")


if BryceWren == '__main__':
    pass
