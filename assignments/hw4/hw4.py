from graphics import *
import math
def squares():
    window = GraphWin("Squares", 700, 700)
    for i in range(1, 6):
        circle = Circle(window.getMouse(), 50)
        cornerPointa = circle.getP1()
        cornerPointb = circle.getP2()
        rectangle = Rectangle(cornerPointa, cornerPointb)
        rectangle.draw(window)
        rectangle.setFill("red")
    click_text = Text(Point(350,350), "Click again to close")
    click_text.draw(window)
    window.getMouse()

squares()

def rectangle():
    window = GraphWin("Rectangle", 700, 700)
    rec_point1 = window.getMouse()
    rec_point2 = window.getMouse()
    arectangle = Rectangle(rec_point1, rec_point2)
    arectangle.setFill("green")
    y = rec_point1.getY()
    y2 = rec_point2.getY()
    x = rec_point1.getX()
    x2 = rec_point2.getX()
    print(x, y)
    print(x2, y2)
    height = abs(y2 - y)
    length = abs(x - x2)
    perimeter = "perimeter:", height * 2 + length * 2
    area = "area:", height * length
    p_text = Text(Point(350, 625), perimeter)
    a_text = Text(Point(350, 650), area)
    a_text.draw(window)
    p_text.getAnchor()
    p_text.draw(window)
    arectangle.draw(window)
    click_text = Text(Point(350, 50), "Click again to close")
    click_text.draw(window)
    window.getMouse()
rectangle()

def circle():
    win = GraphWin("Circle", 700, 700)
    x = win.getMouse()
    sus = win.getMouse()
    x_two = sus.getX()
    x_one =x.getX()
    y_one =x.getY()
    y_two =sus.getY()
    radius = math.sqrt((x_two - x_one)**2 + (y_one - y_two)**2)
    radius_2 = "radius:", radius
    circle_a= Circle(x, radius)
    circle_a.getRadius()
    circle_a.draw(win)
    textimizer = Text(Point(350, 675), radius_2)
    textimizer.draw(win)
    click_text = Text(Point(350,650), "click to close!")
    click_text.draw(win)
    win.getMouse()
circle()

def pi2():
    user = eval(input("how many terms to sum?"))
    num = 1
    approx = 0
    denom = 1
    for i in range(user):
        numerator = 4
        approx = approx + (numerator/denom) * num
        denom = denom + 2
        num = num * -1
    approx_pi = approx
    accuracy = approx_pi - math.pi
    print("pi approximation:", approx_pi)
    print("accuracy:", abs(accuracy))
    print(denom)

pi2()
