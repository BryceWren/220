import graphics

point_a = graphics.Point(50, 70) # Constructors
point_b = graphics.Point(90, 100) # x and y are floats
x = point_a.getX()
x_b = point_b.getX()
print(x_b)
print(type(x_b))

    # takes parameters aka initial data
    # creating an instance of this object
# print(type(point_a))

# methods are functions that relate to a class in some way
    # they use instanced variables to for a function

point_a = graphics.Point(50, 70) # the .Point is the Constructors
# 50, and 70 are my variables
point_b = graphics.Point(90, 100)
print(point_a.getX(), point_a.getY()) # accessor methods, getX() is a method
point_a.move(10, 0)
print(point_a.getX(), point_a.getY())

win = graphics.GraphWin("CSCI 220", 700, 700) # "Title",x , y
point_a.draw(win)
middle = graphics.point(350,350)
print = middle.draw(win)


my_circle = graphics.Circle(middle, 70)
my_circle.draw("hit enter to exit")
# a circle object will that a center and a radius

input("hit enter to exit")
#a Graph has a title aka. a string, height defaults to 200, and width defaults to 200

#import graphics
from graphics import Point, GraphWin, Circle

