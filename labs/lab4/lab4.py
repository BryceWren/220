from graphics import *
import time


def valentines():
    win = GraphWin("Valentines", 500, 500)
    left_circle = Circle(Point(200,100), 60)
    r_circle = left_circle.clone()
    r_circle.move(100, 0)
    left_circle.setFill("Red")
    left_circle.setOutline("Red")
    left_circle.draw(win)
    r_circle.setFill("Red")
    r_circle.draw(win)
    r_circle.setOutline("Red")
    text_v = Text(Point(250, 450), "Happy Valentine's Day!")
    r_rectangle = Rectangle(Point(100, 150), Point(300, 150))
    r_rectangle.move(-99, 0)
    r_rectangle.draw(win)
    a_triangle = Polygon(Point(300,140), Point(300, 160), Point(310, 150))
    a_triangle.move(-99,0)
    a_triangle.draw(win)
    a_triangle.setFill("black")
    h_triangle = Polygon(Point(150, 100), Point(350, 100), Point(250, 300))
    h_triangle.setFill("Red")
    h_triangle.setOutline("Red")
    h_triangle.draw(win)
    text_v.draw(win)
    for i in range(15):
        a_triangle.move(10, 0)
        r_rectangle.move(10, 0)
        time.sleep(.5)
    close_text = Text(Point(250,475),"Click to Close!")
    close_text.draw(win)
    win.getMouse()


valentines()