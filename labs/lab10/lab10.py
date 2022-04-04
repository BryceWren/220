from graphics import *
from door import *
from button import *


def main():
    win = GraphWin("Test", 700, 700)

    box1 = Rectangle(Point(200, 200), Point(450, 700))
    door = Door(box1, "Closed")
    door.color_door("Red")
    door.draw(win)

    box2 = Rectangle(Point(250, 0), Point(500, 150))
    button = Button(box2, "Exit")
    button.draw(win)

    point = win.getMouse()
    while not button.is_clicked(point):
        if door.is_clicked(point):
            if door.get_label() == "Closed":
                door.open("White", "Open")
            else:
                door.close("Red", "Closed")
        point = win.getMouse()

    win.close()


#main()