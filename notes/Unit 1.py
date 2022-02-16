def future():
    age = eval(input('enter your age:'))
    futureage = age + 20
    print('in 20 years you will be', futureage)

def convert():
    # <--- is a comment, aka a number symbol. ( this is overlooked by the computer and is just for the programmer)
    # get user input in celsius
    celsius = eval(input('enter temp in celsius'))
    # convert input from celsius to fahrenheit using the equation c x (9/5) + 35
    fahrenheit = celsius * 9 / 5 + 32
    x = 10
    y = "hey" # is a literal
    # display result to user
    print('that is', fahrenheit)
    # ** = raised power ex. 2^2
    # others are + - / *



def principal_apr():
    principal = eval(input('enter principal balance'))
    apr = eval(input("enter interest rate:"))
    for _ in range(10):
        principal = principal * (1 + apr)
        print(principal)
        print("the final balance is", principal)

for i in range(5):
    # range(5) means 0,1,2,3,4
    # i = 0
    for j in range(5):
        # j = 0
        print(i, j, end ='-')
        # it prints 0 0 - 0 1 - 0 2 - 0 3 - 0 4 -
    print()
    # new time through loop j starts @ 0
    # prints 1 0 - 1 1 - 1 2 - 1 3 - 1 4
    # print 2 0 - 2 1 - 2 2 - 2 3 - 2 4
    # THESE ARE NESTED LOOPS

#CHAPTER 3: DATA TYPES

# "HELLO WORLD" IS A STRING
# data types effect functionality of code
for i in range(3):
    print(i)
    # THIS IS WRONG because this 3 is not in parenthesis so it is not considered a sequence

for pp in range(3):
    print(pp)

    #3 - int/integer + // - , a whole number
        # // is integer division
    #30 - float/ +/-, are decimals
    # % sign is called mod/ modular arrithmatic
    #

for i in range(10)
