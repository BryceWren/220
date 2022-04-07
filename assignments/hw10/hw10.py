"""
Name: <Bryce Wren>
Assignment description:
"""

def fibonacci(n):
    n_one = 0
    n_two = 1
    count = 0
    if n <= 0:
        return None
    else:
        while count < n:
            new_one = n_one + n_two
            n_one = n_two
            n_two = new_one
            count += 1
        return n_one

def double_investment(principle, rate):
    acc = 0
    #annual = 0
    final = 0
    while final <= principle * 2:
        acc += 1
        annual = (principle * (1 + rate))
        final += annual * (1 + rate)
    print(acc)

double_investment(26319, .18) # = 5

# we want to store the principle each time with the investment 1000 - > 1070
def syracuse(n):
    my_list = [n]
    while n != 1:
        if n % 2 == 0:
            n = n/2
            my_list.append(n)
        else:
            n = 3 * n + 1
            my_list.append(n)
    return my_list


def prime(num):
    if num % 2 == 0:
        return True
    else:
        return False


def goldbach(n):
    nums = 0
    my_list = []
    for i in range(1, n + 1): # while n < nums
        if prime(i):
            nums += 1
            my_list.append(i)
        for first_num in my_list:
            for second_num in my_list:
                x = first_num + second_num
                if x == n:
                    return[first_num, second_num]
    if n % 2 != 0:
        return None

from face import Face
from graphics import *
#Face.smile()

