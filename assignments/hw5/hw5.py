
"""
Name: <Bryce Wren>
<ProgramName>.py

Problem: <using lists and slicing to solve problems>

Certification of Authenticity:
<include one of the following>
I certify that this assignment is entirely my own work.
"""

def name_reverse():
    name = input("What is your name (first last)")
    x = name.split()
    l_name = x[1]
    f_name = x[0]
    print(l_name.rstrip() + ",", f_name.rstrip())

#name_reverse()

def company_name():
    domain = input("enter a domain:")
    x = domain.split(".")
    company = x[1]
    print(company)
#company_name()

def initials():
    students = eval(input("how many students are in the class?"))
    num = ' '
    for i in range(1, students + 1):
        name = input("what is the name of student {}".format(i))
        x = name.split()
        extra = x[0]
        first_i = extra[0]
        simple = num + x[1]
        last_i = simple[1]
        print(first_i + last_i)

#initials()

def names():
    user = input("enter a list of names:")
    lip = user.split(",")
    lips = len(lip) - 1
    num = " "
    for i in range(0, lips + 1):
        niel = lip[i].split()
        niel_0 = niel[0]
        niel_1 = niel[1]
        inside_string_1 = num + niel_0[0]
        inside_string_2 = num + niel_1[0]
        final = (inside_string_1.strip()+inside_string_2.strip())
        print(final.strip(), end="\t")

#names()

def thirds():
    n_sentences = eval(input("enter the number of sentences:"))
    stuff = []
    for i in range(1, n_sentences + 1):
        sentence = input("enter sentence {} :".format(i))
        x = sentence[0::3]
        (stuff.append(x))
    for item in stuff:
        print(item)

#thirds()

def word_average():
    sentence = input("enter a sentence:")
    words = sentence.split()
    count = len(words) - 1
    num = sentence[0:]
    nums = len(num) - count
    average = nums / len(words)
    print(average)


#word_average()

def pig_latin():
    user = str(input("enter a sentence to convert to pig latin:"))
    sentence_split = user.split()
    for i in sentence_split:
        word = (i[1:] + i[0] + "ay")
        print(word.lower(), end=" ")
# Output works on its own but doesn't work going through the test file
#pig_latin()

if __name__ == '__main__':
    pass
