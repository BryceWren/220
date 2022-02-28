"""
Name: <Bryce Wren>
<hw6>.py

Problem: <using strings to write encryptions as well as developing functions>

Certification of Authenticity:
<include one of the following>
I certify that this assignment is entirely my own work.
"""

import math

def cash_converter():
    money = eval(input("enter an integer:"))
    money_final = ("that is ${:.2f}".format(money))
    print(money_final)

def encode():
    user = str(input("enter a message:"))
    key = eval(input("enter a key:"))
    encoded_string = ""
    for character in user: #"enter that string"
        code_character = (ord(character) + key)
        # takes a string character by character then gives a number and adds key to it
        enc_let = (chr(code_character))
        # converts the unicode from an integer to a chracter
        encoded_string = encoded_string + enc_let
    print(encoded_string)


def sphere_area(radius):
    area = 4 * math.pi * radius**2
    return area


def sphere_volume(radius):
    volume = (4/3) * math.pi * radius**3
    return volume


def sum_n(number):
    initiator = 0
    for i in range(1, number + 1):
        initiator = initiator + i
    return initiator

def sum_n_cubes(number):
    initiator = 0
    for i in range(1, number + 1):
        initiator = initiator + i**3
    return initiator

def encode_better():
    user = input("enter a message:")
    key = input("enter a key:")
    encoded_string = ""
    for number in range(len(user)):
        code_character = ord(user[number]) - 65
        index_key = (number % len(key))
        key_string = key[index_key]
        key_number = ord(key_string) - 65
        difference_value = (code_character + key_number) % 58
        value_letter = difference_value + 65
        encoded_string = encoded_string + chr(value_letter)
    print(encoded_string)




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
