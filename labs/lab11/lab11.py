from random import randint
from graphics import *
from labs.lab10.door import Door
from labs.lab10.button import Button


def main():
    win = GraphWin("Door Game", 1000, 1000)
    box1 = Rectangle(Point(300, 200), Point(550, 700))
    door1 = Door(box1, "Closed")
    door1.color_door("Red")
    door1.draw(win)

    box2 = box1.clone()
    box2.move(300, 0)
    door2 = Door(box2, "Closed")
    door2.color_door("Red")
    door2.draw(win)

    box3 = box1.clone()
    box3.move(-300, 0)
    door3 = Door(box3, "Closed")
    door3.color_door("Red")
    door3.draw(win)

    box4 = Rectangle(Point(250, 0), Point(500, 150))
    button = Button(box4, "Exit")
    button.draw(win)

    point = win.getMouse()
    door_list = [door1, door2, door3]

    wins = 0
    loss = 0

    score_board = Rectangle(Point(50, 0), Point(200, 100))
    score_board_real = Button(score_board, wins)
    score_board_real.draw(win)

    while not button.is_clicked(point):
        random_num = randint(0, 2)
        ran_door = door_list[random_num]
        ran_door.set_secret(True)
        for door in door_list:
            if door.is_secret() and door.is_clicked(point):
                door.color_door("Green")
                wins += 1


            elif not door.is_secret() and door.is_clicked(point):
                door.color_door("Brown")
                loss += 1
            elif door.is_secret() and not door.is_clicked(point):
                door.color_door("Green")

        play_again_text = Text(Point(100, 800), "click to play again")
        play_again_text.draw(win)
        # click anywhere to play again


        for door in door_list:
            door.color_door("Red")


        # point = win.getMouse()
        # x = Text("0", Point(50, 50))
        # x.setText(win)
        # x.draw()


main()
