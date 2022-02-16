import math
import graphics
from graphics import Point, GraphWin, Circle, Text, Entry

win = GraphWin('face', 700, 700) # Title, Width, Height
win.setCoords(0, 0, 10, 10)
# redifining the coords (x, y value of lower left corner) (x, y value of the upper right corner)
face = Circle(Point(5, 7), 3) # (Center of Circle, Radius)
name = Text(Point(3, 1), "Bob") # (where the text should appear, what the text says)
name.draw(win)
user_input = Entry(Point(5, 5), 30)
user_input.setText("Enter Name")
user_input.draw(win)
win.getMouse()
name = user_input.getText()
print(name)
# message.setText # lets you change what the text says after everything has been done

left_eye = Circle(Point(325, 60), 25)
left_eye.setFill("yellow")
left_eye.setOutline("green")
left_eye.setWidth(5) # Order matters
right_eye = left_eye.clone() # clone returns a new circle therefore not resulting in memory mess up
right_eye.move(50, 0)


# center = right_eye.getCenter().getX()
# getX method returns a float, getCenter() returns a point.
# center.getX()

# print(left_eye.getCenter().getX())
# print(right_eye.getCenter().getX())

#

face.draw(win)
left_eye.draw(win)
right_eye.draw(win)
left_eye.dra
# input("enter")

click_point = win.getMouse() # returns a point object this can also be called an event
# print(click_point.getX(), click_point.getY())
# you can look at python api on OAKS

def convert():
    win = GraphWin("Converter", 700, 500)
    win.setCoords((0, 0, 10, 10))
    celsius_text = Text(Point(3, 8), "Celsius")
    celsius_entry = Entry(Point(7, 8), 30)
    click_text = Text(Point(5, 5), "Click to Convert")
    result_text = Text(Point(3, 1), " ")

    celsius_text.draw(win)
    celsius_entry.draw(win)
    click_text.draw(win)
    result_text.draw(win)
    win.getMouse()
    celsius = eval(celsius_entry.getText())
    farenheit = celsius * 9 / 5 + 32
    result_text.setText(farenheit)
    click_text.setText("Click to Close!")

    win.getMouse()


