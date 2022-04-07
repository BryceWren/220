from random import randint
from graphics import *


def get_words(file_name):
    open_file = open(file_name, 'r')
    reading_file = open_file.readlines()
    return reading_file


def get_random_word(words):
    random_index = randint(0, len(words) - 1)
    for i in range(len(words)):
        random_words = words[random_index]
        no_new_line_word = random_words[:-1]
        return no_new_line_word


def letter_in_secret_word(letter, secret_word):
    for i in secret_word:
        if letter == i:
            return True
    return False


def already_guessed(letter, guesses):
    for i in guesses:
        if letter == i:
            return True
    return False


def make_hidden_secret(secret_word, guesses):
    empty_string = ""
    for letter in secret_word:
        if letter in guesses:
            empty_string += letter + " "
        else:
            empty_string += "_ "
    empty_string = empty_string[:-1]
    return empty_string


def won(guessed):
    for i in guessed:
        if i == "_":
            return False
    return True

# open a terminal
    # won("_h__")
    # won("hello")
    # won(h___o)

def change_color(win, letter, alphabet):
    window = win
    for i in alphabet:
        text_alphabet = Text(Point(350, 20), alphabet)
        if letter == i:
            color = text_alphabet.setFill("White")
        text_alphabet.draw(win)


def play_graphics(secret_word):

    win = GraphWin("hangman", 700, 700)
    win.setBackground("White")
    text_letter = Text(Point(250, 650), "enter a letter:")
    text_letter.draw(win)
    user_entry = Entry(Point(350, 650), 5)
    user_entry.draw(win)
    base = Line(Point(250, 600), Point(500, 600))
    base.draw(win)
    stand = Line(Point(375, 600), Point(375, 100))
    stand.draw(win)
    slant_stand = Line(Point(375, 100), Point(250, 200))
    slant_stand.draw(win)
    alphabet = "a b c d e f g h i j k l m n o p q r s t u v w x y z"

    head = Circle(Point(250, 250), 50)
    torso = Line(Point(250, 300), Point(250, 400))
    left_leg = Line(Point(250, 400), Point(200, 500))
    right_leg = Line(Point(250, 400), Point(200, 550))
    right_arm = Line(Point(250, 350), Point(300, 350))
    left_arm = Line(Point(250, 350), Point(200, 350))

    acc = 7
    guess_list = []
    text_hidden_word = Text(Point(250, 550), hidden_secret)
    text_hidden_word.draw(win)
    while True:
        hidden_secret = make_hidden_secret(secret_word, guess_list)
        win.getMouse()
        user_guess = user_entry.getText()
        text_hidden_word.setText(hidden_secret)
        change_color(win, user_guess, alphabet)
        guess_list.append(user_guess)
        color_change = Text(Point(250, 250), guess_list)
        color_change.draw(win)
        hidden_secret = make_hidden_secret(secret_word, guess_list)
        if not letter_in_secret_word(user_guess, secret_word) or not already_guessed(user_guess, guess_list):
            acc = acc - 1
        #attempts = "guesses remaining: {}".format(acc)
        #print("already guessed: {}".format(guess_list))
        #print(attempts)
        if acc == 0 or won(hidden_secret):
            break
        if acc == 7:
            win.getMouse()
        if acc == 6:
            head.draw(win)
        if acc == 5:
            torso.draw(win)
        if acc == 4:
            left_arm.draw(win)
        if acc == 3:
            right_arm.draw(win)
        if acc == 2:
            right_leg.draw(win)
        if acc == 1:
            left_leg.draw(win)
    if won(hidden_secret):
        print("winner!")

    else:
        print("i regret to inform you that you have lost. the word was {}".format(secret_word))

    win.getMouse()

play_graphics("time")

def play_command_line(secret_word):
    acc = 7
    guess_list = []
    while True:
        hidden_secret = make_hidden_secret(secret_word, guess_list)
        print(hidden_secret)
        user_guess = input("guess a letter:")
        guess_list.append(user_guess)
        hidden_secret = make_hidden_secret(secret_word, guess_list)
        if not letter_in_secret_word(user_guess, secret_word) or not already_guessed(user_guess, guess_list):
            acc = acc - 1
        attempts = "guesses remaining: {}".format(acc)
        print("already guessed: {}".format(guess_list))
        print(attempts)
        if acc == 0 or won(hidden_secret):
            break
    if won(hidden_secret):
        print("winner!")
        print(hidden_secret)
    else:
        print("i regret to inform you that you have lost. the word was {}".format(secret_word))


#playcommand_line("time")
if __name__ == '__main__':
    pass
    # play_command_line(secret_word)
    # play_graphics(secret_word)

#text object:
    #text
    #a = text(Point(3,4), "h")
    text = "hi"
    # Set text replaces the original property and changes the value

