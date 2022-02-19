import math


def sequence():
    term = eval(input("how many terms would you like?"))
    for i in range(1, term + 1):
        num = (i % 2)+ i - 1
        print(num, end= " ")

from math import *
def test():
    user = eval(input("how many terms to sum?"))
    num = 0
    approx = 1
    for i in range(1, user + 1):
        numerator = 1
        denom = (1 // i) + 2
        approx = approx * (numerator/denom)
    approx_pi = 4 * approx + 2
    accuracy = approx_pi - math.pi
    print("pi approximation:", approx_pi)
    print("accuracy:", accuracy)

#test()
