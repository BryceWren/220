# look at circle overlap for when the circles hit
from random import randint
from graphics import *
import math


def get_random(move_amount):
    random_move = randint(-move_amount, +move_amount)
    return random_move


def did_collide(circle_ball, circle_ball2):
    x_one = circle_ball.getCenter().getX()
    y_one = circle_ball.getCenter().getY()
    x_two = circle_ball2.getCenter().getX()
    y_two = circle_ball2.getCenter().getY()
    distance_f = math.sqrt((x_two - x_one) ** 2 + (y_two - y_one) ** 2)
    circle_ball_radius = circle_ball.getRadius()
    circle_ball2_radius = circle_ball2.getRadius()
    if circle_ball2_radius + circle_ball_radius > distance_f:
        return True
    else:
        return False


def hit_vertical(circle_ball, win):
    ball_radius = circle_ball.getRadius()
    if ball_radius < circle_ball.getCenter().getX() < win.getWidth() - ball_radius:
        return False
    else:
        return True


def hit_horizontal(circle_ball, win):
    ball_radius = circle_ball.getRadius()
    if ball_radius < circle_ball.getCenter().getY() < win.getHeight() - ball_radius:
        return False
    else:
        return True


def get_random_color():
    random_color = randint(0, 255)
    random_color2 = randint(0, 255)
    random_color3 = randint(0, 255)
    final_color = color_rgb(random_color, random_color2, random_color3)
    return final_color

def bumper_car_simulation():
    width_px = 700
    height_px = 700
    win = GraphWin("Circle", width_px, height_px)

    center = Point(200, 200)
    radius = 50
    circle_one = Circle(center, radius)
    circle_one.setFill(get_random_color())

    center = Point(500, 500)
    radius = 50
    circle_two = Circle(center, radius)

    circle_two.draw(win)
    circle_one.draw(win)
    circle_two.setFill(get_random_color())
    dx = get_random(10)
    dy = get_random(10)
    dx_two = get_random(10)
    dy_two = get_random(10)

    while not win.checkMouse():
        circle_one.move(dx, dy)
        circle_two.move(dx_two, dy_two)
        if did_collide(circle_one, circle_two):
            dx = dx * -1
            dy = dy * -1
            dx_two = dx_two * -1
            dy_two = dy_two * -1
        if hit_vertical(circle_one, win):
            dx = dx * -1
        if hit_vertical(circle_two, win):
            dx_two = dx_two * -1
        if hit_horizontal(circle_one, win):
            dy = dy * -1
        if hit_horizontal(circle_two, win):
            dy_two = dy_two * -1
        time.sleep(.10)

    win.close()

bumper_car_simulation()