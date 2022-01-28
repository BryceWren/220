"""
Name: <Bryce Wren>
<ProgramName>.py

Problem: <Making for loops and (math.) functions in order to get functions to create solutions for problems>

Certification of Authenticity:
<include one of the following>
I certify that this assignment is entirely my own work.
"""
import math


def sum_of_threes():
    user_input = eval(input('What is the upper bound?'))
    sum = 0
    for i in range(3,user_input + 1,3):# loop starts at 3 but stops at the upper bound where the user inputs, then steps
        # every 3
        sum = (sum + i)
    print("sum of threes is", sum)


def multiplication_table():
    for i in range(1,11): # using a nested for loop
        for j in range(1,11):
            print(i * j, end = '\t') # multiplying both loops and spacing them out using \t
        print()

def triangle_area():
    variable_a = eval(input('Enter side a length:'))
    variable_b = eval(input('Enter side b length:'))
    variable_c = eval(input('Enter side c length:'))
    s = (variable_a + variable_b + variable_c)/2
    area = math.sqrt(s*(s-variable_a)*(s-variable_b)*(s-variable_c))
    print('area is:',area)


def sum_squares():
    lower = eval(input('Enter lower range:'))
    upper = eval(input('Enter upper range:'))
    sum = 0
    for i in range(lower, upper + 1):
        sum = sum + (i**2) # change the sum variable to be the 0 + (the i loop ^2)
    print(sum)


def power():
    base = eval(input('enter base:'))
    exponent = eval(input('enter exponent:'))
    exp = 1
    for i in range(exponent): # the exponent is the number of times you loop
        exp = exp * base # using multiplication because of what an exponent does by multiplying the base 3 times.
    print(base, '^', exponent,'=',exp)

if __name__ == '__main__':
    pass
