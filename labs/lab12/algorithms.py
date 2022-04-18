"""
LINEAR SEARCH
"""

def read_data(filename):
    open_file = open(filename, "r")
    read_file = open_file.readline()
    my_list = []
    while read_file:
        split_line = read_file.split(" ")
        acc = 0
        while split_line:
            my_list.append(split_line[acc])
            acc += 1
        # for each line i need to change it to a integer or float

def is_in_linear(search_val, values):
    i = 0
    found = False
    while i <= len(values) - 1 and not found:
        if search_val == values[i]:
            found = True
            return found
        else:
            i += 1
            return found