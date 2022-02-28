from graphics import *

def encode():
    user = (input("enter a message:"))
    message = (user.split())
    key = eval(input("enter a key:"))
    word = 0
    num = ""
    print(message)
    for number in message: #['the', 'dog']
        letter = (ord(number) + key) #gives a number then adds key to it
        word = word + (letter) #keeps the numbers an integer so its easily deciphered later in loop
        enc_let = (chr(letter)) #changes the new unicode number to a different letter
        num = num + enc_let + " " # makes the letter a string so it is able to print
    print(num)
    print(ord(number))
    print(message)
#encode()


def test():
    user = (input("enter a message:"))
    message = user.join("[]")
    print(message)
    print(type(message))

test()