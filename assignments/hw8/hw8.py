"""
Name: <your name goes here – first and last>
<ProgramName>.py

Problem: <Brief, one or two sentence description of the problem that this program solves, in your own words.>

Certification of Authenticity:
<include one of the following>
I certify that this assignment is entirely my own work.
I certify that this assignment is my own work, but I discussed it with: <Name(s)>
"""
from graphics import *
import math


def add_ten(nums):
    for i in range(len(nums)):
        nums[i] = (nums[i] + 10)


def square_each(nums):
    for i in range(len(nums)):
        nums[i] = (nums[i]**2)


def sum_list(nums):
    sumation = 0
    for i in range(len(nums)):
        sumation += nums[i]
    return sumation


def to_numbers(nums):
    for i in range(len(nums)):
        nums[i] = float(nums[i])


def sum_of_squares(nums):
    my_list = []
    for items in nums:
        split_list = items.split(", ")
        to_numbers(split_list)
        square_each(split_list)
        my_list.append(sum_list(split_list))
    return my_list


def starter(weight, wins):
    if weight >= 150 and weight < 160 and wins >= 5:
        return True
    elif weight > 199 or wins > 20:
        return True
    return False


def leap_year(year):
    if year % 100 == 0 and year % 400 != 0:
        return False
    elif year % 4 == 0:
        return True
    return False


def did_overlap(circle_one, circle_two):
    x_one = circle_one.getCenter().getX()
    y_one = circle_one.getCenter().getY()
    x_two = circle_two.getCenter().getX()
    y_two = circle_two.getCenter().getY()
    distance_f = math.sqrt((x_two - x_one)**2 + (y_two - y_one)**2)
    circle_one_radius = circle_one.getRadius()
    circle_two_radius = circle_two.getRadius()
    sum_radius = circle_one_radius + circle_two_radius
    print(sum_radius)
    print(distance_f)
    if sum_radius >= distance_f:
        return True
    else:
        return False

def circle_overlap():
    width_px = 700
    height_px = 700
    win = GraphWin("Circle", width_px, height_px)
    width = 10
    height = 10
    win.setCoords(0, 0, width, height)

    center = win.getMouse()
    circumference_point = win.getMouse()
    radius = math.sqrt(
        (center.getX() - circumference_point.getX()) ** 2 + (center.getY() - circumference_point.getY()) ** 2)
    circle_one = Circle(center, radius)
    circle_one.setFill("light blue")
    circle_one.draw(win)

    center2 = win.getMouse()
    circumference_point_two = win.getMouse()
    radius_two = math.sqrt(
        (center2.getX() - circumference_point_two.getX()) ** 2 + (center2.getY() - circumference_point_two.getY()) ** 2)
    circle_two = Circle(center2, radius_two)
    circle_two.setFill("light green")
    circle_two.draw(win)

    win.getMouse()

    result = did_overlap(circle_one, circle_two)

    if result is True:
        Text(Point(2, 3), "The circles overlap.").draw(win)
    else:
        Text(Point(2, 3.5), "The circles do not overlap.").draw(win)

    Text(Point(2, 2), "Click to close")

    win.getMouse()


circle_overlap()



if __name__ == '__main__':
    pass
