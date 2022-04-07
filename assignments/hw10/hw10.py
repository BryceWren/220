"""
Name: <Bryce Wren>
Assignment description:
"""

import math

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
    annual = principle
    while annual <= principle * 2:
        acc += 1
        annual = (annual * (1 + rate))
    return acc


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
    n = 2
    while int(math.sqrt(num)) % n != 0 and n < int(math.sqrt(num)):
        if int(math.sqrt(num)) % n == 0:
            return False
        n += 1
    else:
        return True


def goldbach(num):
    nums = 0
    i = 0
    my_list = []
    while nums < num:
        if prime(nums):
            my_list.append(nums)
            nums += 1
    while True:
        first_num = my_list[i]
        second_num = my_list[i + 1]
        sum_num = first_num + second_num
        if second_num > len(my_list):
            break
        if sum_num == num:
            break
        return[first_num, second_num]
    i += 1

    if num % 2 != 0:
        return None

goldbach(5)
from face import Face
from graphics import *
#Face.smile()

