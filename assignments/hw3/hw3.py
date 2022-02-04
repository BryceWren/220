"""
Name: <Bryce Wren>
<ProgramName>.py

Problem: <using loops to solve for sequences and finding approximations .>

Certification of Authenticity:
<include one of the following>
I certify that this assignment is entirely my own work.
"""


def average():
    grade_number = eval(input("How many grades will you enter"))
    num = 0
    for i in range(grade_number):
        grade = eval(input("enter grade"))
        num = num + grade
    final_average = num / grade_number
    print("average is", final_average)


def tip_jar():
    people = 5
    zero = 0
    for i in range(people):
        amount = eval(input("how much would you like to donate?"))
        zero = zero + amount
    print("total tips:", zero)


def newton():
    x = eval(input("What number do you want to square root?"))
    num = eval(input("How many times should we improve the approximation"))
    approx = x
    for i in range(num):
        esp = approx + (x / approx)
        approx = esp / 2
    print(approx)


def sequence():
    term = eval(input("how many terms would you like?"))
    for i in range(1, term + 1):
        num = (i % 2) + i - 1
        print(num, end=" ")


def pi():
    pi_variable = eval(input("how many terms"))
    approx = 1
    denom = 1
    for i in range(pi_variable):
        numer = (2 * (i // 2)) + 2
        approx = approx * (numer / denom)
        denom = (2 * (i // 2)) + 3
    approx_pi = 2 * approx
    print(approx_pi)



if __name__ == '__main__':
    pass
