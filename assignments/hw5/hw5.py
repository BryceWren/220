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
        print("what is the name of student", i)
        name = input()
        x = name.split()
        extra = x[0]
        first_i = extra[0]
        simple = num + x[1]
        last_i = simple[1]
        print(first_i.upper() + last_i.upper())

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
        x = num + niel_0[0]
        y = num + niel_1[0]
        sick = (x.strip()+y.strip())
        print(sick.upper().strip(), end="\t")

#names()

def thirds():
    n_sentences = eval(input("enter the number of sentences:"))
    stuff = []
    for i in range(1, n_sentences + 1):
        print("enter sentence", i, ":")
        sentence = input()
        x = sentence[0::3]
        (stuff.append(x))
    for item in stuff:
        print(item.capitalize())

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
        word = i[1:] + i[0] + "ay"
        print(word.lower(), end=" ")

#pig_latin()