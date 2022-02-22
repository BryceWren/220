from graphics import *
import math

def triange():
    window = GraphWin("Triangle", 700, 700)
    poly_1 = window.getMouse()
    poly_2 = window.getMouse()
    poly_3 = window.getMouse()
    triangle_2 = Polygon(poly_1, poly_2, poly_3)
    x1 = poly_1.getX()
    y1 = poly_1.getY()
    x2 = poly_2.getX()
    y2 = poly_2.getY()
    x3 = poly_3.getX()
    y3 = poly_3.getY()
    line_1x = x2 - x1
    line_1y = y2 - y1
    line_2x = x3 - x1
    line_2y = y3 - y1
    line_3x = x3 - x2
    line_3y = y3 - y2
    length_line1 = math.sqrt(math.pow(line_1x, 2) + math.pow(line_1y, 2))
    length_line2 = math.sqrt(math.pow(line_2x, 2) + math.pow(line_2y, 2))
    length_line3 = math.sqrt(math.pow(line_3x, 2) + math.pow(line_3y, 2))
    perimeter = "Perimeter:", length_line1 + length_line2 + length_line3
    s = (length_line1 + length_line2 + length_line3) / 2
    area = "Area:", math.sqrt(s * (s - length_line1)*(s - length_line2)*(s - length_line3))
    triangle_2.draw(window)
    t_per = Text(Point(350, 650), perimeter)
    t_area = Text(Point(350, 675), area)
    t_per.draw(window)
    t_area.draw(window)

    print(perimeter)
    print(area)
    print(s)
    window.getMouse()
#triange()

def color_shape():
    '''Create code to allow a user to color a shape by entering rgb amounts'''

    # create window
    win_width = 400
    win_height = 400
    win = GraphWin("Color Shape", win_width, win_height)
    win.setBackground("white")

    # create text instructions
    msg = "Enter color values between 0 - 255\nClick window to color shape"
    inst = Text(Point(win_width / 2, win_height - 20), msg)
    inst.draw(win)

    # create circle in window's center
    shape = Circle(Point(win_width / 2, win_height / 2 - 30), 50)
    shape.draw(win)

    # redTexPt is 50 pixels to the left and forty pixels down from center
    red_text_pt = Point(win_width / 2 - 50, win_height / 2 + 40)
    red_text = Text(red_text_pt, "Red: ")
    red_text.setTextColor("red")

    # green_text_pt is 30 pixels down from red
    green_text_pt = red_text_pt.clone()
    green_text_pt.move(0, 30)
    green_text = Text(green_text_pt, "Green: ")
    green_text.setTextColor("green")

    # blue_text_pt is 60 pixels down from red
    blue_text_pt = red_text_pt.clone()
    blue_text_pt.move(0, 60)
    blue_text = Text(blue_text_pt, "Blue: ")
    blue_text.setTextColor("blue")

    #red Entry boxes
    red_point = red_text_pt.clone()
    red_point.move(50, 0)
    red_entry = Entry(red_point, 5)
    red_entry.draw(win)

    #green entry box
    green_point = green_text_pt.clone()
    green_point.move(50, 0)
    green_entry = Entry(green_point, 5)
    green_entry.draw(win)

    #blue entry boxes
    blue_point = blue_text_pt.clone()
    blue_point.move(50, 0)
    blue_entry = Entry(blue_point, 5)
    blue_entry.draw(win)



    # display rgb text
    red_text.draw(win)
    green_text.draw(win)
    blue_text.draw(win)

    for i in range(5):
        win.getMouse()
        user_b = int(blue_entry.getText())
        user_g = int(green_entry.getText())
        user_r = int(red_entry.getText())
        shape.setFill((color_rgb(user_r, user_b, user_g)))

    # Wait for another click to exit
    win.getMouse()
    win.close()

#olor_shape()
def process_string():
    x = input("input a string")
    print(x[0])
    print(x[-1])
    print(x[1:4])
    print(x[0] + x[-1])
    print(x[0] * 10)
    for i in x:
        print(i)
    print(len(x))

def process_list():
    pt = Point(5, 10)
    values = [5, "hi", 2.5, "there", pt, "7.2"]
    x = values[1] + values[3]
    print(x)
    x = values[0] + values[2]
    print(x)
    x = values[1] * 5
    print(x)
    x = values[2], values[3], str(pt)
    print(x)
    x = values[2], values[3], values[0]
    print(x)
    x = values[2], values[0], float(values[-1])
    print(x)
    x = float(values[0]) + float(values[2]) + float(values[-1])
    print(x)
    x = len(values)
    print(x)

#process_list()
def another_series():
    inputs = eval(input("how many terms?"))
    num = 0
    for i in range(inputs):
        seq = (i % 3) * 2 + 2
        num = num + seq
        print(seq, end="\t")
    print("\n""sum = {}".format(num).center(10))
#another_series()
def target():
    color = ["Yellow", "Red", "Blue", "Black", "White"]
    rad = [225, 175, 125, 75, 25]
    win = GraphWin("target", 500, 500)
    num = 0
    for r in (rad):
        aCircle = Circle(Point(250, 250), r)
        aCircle.setFill(color[num])
        aCircle.draw(win)
        num += 1

    finish_text = Text(Point(250, 10), "Click to Close!")
    finish_text.draw(win)
    win.getMouse()

target()