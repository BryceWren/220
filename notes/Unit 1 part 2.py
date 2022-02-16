# Modular arethmatic
# %
# detecting if something is even or odd
7 % 4
# after doing 7 / 4 then it finds the remainder so it would be 3
9 % 2
# 2 goes into mod 4 times so the remainder will be 1
# % this is remainder after division
for i in range(5):
    print (i % 2)
    # mod is good for a sequences

abs(-10)
# abs is absoulte value

import math

# dot notation
x = math.sqrt(9)
print(x)

x = math.pow(2,3)# parameters | arguments, they are seperated with commas
print(x)

x = math.sqrt(9,25)
print(x)

x = math.sqrt(9) # this is a float in return due to it being 3.0
print(x)

my_range = range(10) # argument says where does it stop
my_range = range(3, 10) # start, stop
my_range = range(3,10,2) # start, stop, step
my_range = range(10,3) # this range is nothing
my_range = range(10,3,-1) # the negative goes down by -1
print(list(my_range))

#DESIGN PATTERNS

# ACCUMULATOR PATTERN
    # A structure when you need to accumulate a result
    # initalizing a variable
my_sum = 0
for i in range(101):
    my_sum = my_sum + i
print(my_sum)

# Factorial 6 !

#Analysis - we want to find the factorial of a #
#specs - input: #, output: factorial, loop and a range, multiplying
#design - get user input, fact = 0, loop from user input -> 1, do factorial * i, then result
#implementation
def factorial():
    user_input = eval(input("enter your number"))
    fact = 1 # when multiplying you need to use 1 because the result would be 0
    for i in range(user_input, 0, -1):
        fact = fact * i
    print(fact)
#test
#debug
import math

def quadratic(): # find the root of a quadratic function
    a = eval(input("What is a"))
    b = eval(input("what is b"))
    c = eval(input('what is c'))
    root_1 = (- b * math.sqrt(b**2 - 4 * a * c))/(2 * a)
    root_2 = (- b * - math.sqrt(b**2 - 4 * a * c))/(2 * a)
    print (root_1, root_2)

#data types
int, float, strings, = # primitive data types
age - 3.5
type(age)
int(age)
round(134314214.1243546355, 3)

# classes are handmade datatypes
    # class is a grouping of data and can contain functions because of different groupings of data
        # range is a class type
            # y = range(10)
        # student class (data)
          # a variable in the class function are called an object
            # object is a specific instance of a class
            # y = range
            #x - range(3,100)
            # type(x) = range
        # x and y are both classes but different objects
            # name - string, age- int, grade 1- float, grade 2-float
        # calculate grade

def class():
    student =

import math
import graphics
    # point class
        # will have an x and y value similar to a map or minecraft
        #class is used to organize data

math.sqrt()

point_a = graphics.Point(50, 70)
print(type(point_a)) # this is a point class, out own object

    #takes two peramiters an x value and a y value