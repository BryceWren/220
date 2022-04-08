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


def syracuse(number):
    my_list = [number]
    while number != 1:
        if number % 2 == 0:
            number = number/2
            my_list.append(number)
        else:
            number = 3 * number + 1
            my_list.append(number)
    return my_list


def prime(num):
    n = 2
    while n <= math.ceil(math.sqrt(num)):
        if num % n == 0:
            return False
        n += 1
    return True



def goldbach(num):
    nums = 0
    i = 0
    my_list = []
    if num % 2 != 0:
        return None
    while nums < num:
        if prime(nums):
            my_list.append(nums)
        nums += 1
    while i < len(my_list):
        if num - my_list[i] in my_list:
            return [my_list[i], num - my_list[i]]
        i += 1
    return None



#goldbach(8368)


