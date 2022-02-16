strings = "strings"
# sequences of characters
list = [1, 2, 3]
# sequences of objects/ within square brackets
# example: strings, Circle objects, integers
#for i in [1, 2, 3]:
    #x = i + 2
    ##3, 4, 5
#b = [1, "paul", "john", 3]
#print(b)

#print(len(b)) #how many elements are in a string or list.
# string: chracters/letters, List: how many objects there are.

# + concatination, join it together
t = "hi" + "john"
print(t)

["ma", "bone"] + ["sell", "structure"]
["ma", "bone", "sell", "structure"]

# when a list has diffeernt data types it such as a string + int = a list as its data type

c = "hi"
d = c * 2
# print will be "hihi"
e = ["mon", "tues"] * 2
# print e = [mon tues mon tues]
f = [1, 2, 3] * 2
# print f = 1 2 3 1 2 3

a = "hello world"
for l in a:
    print(l)

    # l takes each element in the sequence
    #h
    #e
    #l
    #l
    #o etc....

b = ["paul", "george"]
for name in b:
    print(name)
    #paul
    #george

#INDEX VALUES = the position within the sequence
# index always starts at 0
# b = 1
# length of sequence b = 2
# index is the (length of sequence - 1)
# b[0] = how I get paul out of list b

c = [1, 2, "hi", 4][2]
#1 2 3 4
#-4 -3 -2 -1
d = c + 3
print(d)

# substring = group of letters in a string
# subint = group of integers in a list
# slicing =
a[0: 5]
# similar to range
# data type is a string
# when slicing lists it always returns a list

days = ["mon", "tues", "wed", "thurs", "friday" ] # colon = slicing. no colon = indexing

for i in range(100):
    print(days[i % 5]) # index only goes 0 - 4, anything higher will error
    #need to use mod to loop back 0 1 2 3 4 0 1 2 3 4
    #-> i % 2 = 0 or 1
    #-> i # 3 -> 0, 1, 2
    #-> % 4 -> 0, 1, 2, 3
    #-> % 5 -> 0, 1, 2, 3, 4

# any # % 9 -> whatever x is -1 exp. 9-1 so mod will go through 0-8

f_name = (input("enter first name"))
l_name = (input("enter last name"))
f_name[0]
l_name[0:7]
username = f_name + l_name
print(username)


#group of characters you do slicing
months = "JanFebMarAprJunJulAugSepOctNovDec"
months_num = eval(input("enter a month number"))
start = 3 * (months_num - 1)
stop = start + 3
simple = months[start:stop]
print("that is", + simple)

#make months into a list

months = ["January", "feb", "mar", "apr", "jun"]
months_num = eval(input("enter a month number"))
index = months_num - 1
simple = months[index]
print("that is", + simple)

months - ["january", "febuary"]
months = months + ["March"]
months.append("May")

numbers = [] # empty lists, you can append items into the list
for i in range(10):
    number = eval(input("enter number"))
    numbers.append(numbers)

a = "hello stinky"
a.upper() # does not change the a variable
b = a.upper()
print(b)
print(a)
print(b)
c = b.lower()
print(c)

a = "it's a small world after all"
a.capitalize()
print(a) # capitilizes the first letter in the string
a.title()
# capitilizes the first letter in each world
a.count("after") # how many times a pattern is in the string
a.find("all") # finds the index number from left to right
a.rfind("all") # finds the index number from right to left
a.replace('small', 'big')
# replaces the first string with the second
# you can do this with letters numbers or strings
b = ['mon', 'tues', 'wed']
'-'.join(b)
# the string that it opperates on will seperate the components in the list
a.center(50)
# will center it aka how many
a.ljust(50)
#left justified
a.rjust(50)
#right justified
a.lstrip() # takes away spaces
a.split('') # returns a list of strings
my_split = a.split()
my_join = ' '.join(my_split)
my_join
#"its a small world"


#string get stored in memory
# encoding takes letters converts them to numbers and stores them as a binary value
# "a" -> 65
# "b" -> 66
# python uses unicode is a list of mappings
