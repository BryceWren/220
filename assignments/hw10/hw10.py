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
    annual = 0
    while annual <= (principle):
        acc += 1
        annual_intrest = (principle * (1 + rate)) - principle
        annual += annual_intrest
        print(annual)
    return acc

#double_investment(26319, .18)

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

def goldbach(n):

    if n % 2 == 0:

