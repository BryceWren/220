"""
Name: <Bryce Wren>
<hw6>.py

Problem: <Brief, one or two sentence description of the problem that this program solves, in your own words.>

Certification of Authenticity:
<include one of the following>
I certify that this assignment is entirely my own work.
"""


def cash_converter():
    money = eval(input("enter an integer:"))
    money_final = ("that is ${:.2f}".format(money))
    print(money_final)

def encode():
    user = (input("enter a message:"))
    message = str(user.split())
    #key = eval(input("enter a key:"))
    word = ""
    for number in message.split():
        letter = ord(number[0])
        word = word + str(letter) + " "
    print(word.rstrip())

encode()
def sphere_area(radius):
    pass


def sphere_volume(radius):
    pass


def sum_n(number):
    pass


def sum_n_cubes(number):
    pass


def encode_better():
    pass


if __name__ == '__main__':
    # cash_converter()
    # encode()
    # res = sphere_area(13)
    # print(res)
    # res = sphere_volume(13)
    # print(res)
    # res = sum_n(100)
    # print(res)
    # res = sum_n_cubes(13)
    # print(res)
    # encode_better()
    pass
