"""
LINEAR SEARCH
"""

from graphics import *

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
    return my_list
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

def is_in_binary(search_val, values):
    low = 0
    high = len(values) - 1
    mid = 0
    while low <= high:

        mid = (high + low) // 2

        if values[mid] < search_val:
            low = mid + 1
        elif values[mid] > search_val:
            high = mid - 1
        else:
            return True

    return False


def selection_sort(values):
    for i in range(len(values)):
        min_val = i
        for j in range(i, len(values)):
            if values[j] < values[min_val]:
                min_val = j
        if min_val != i:
            temp = values[i]
            values[i] = values[min_val]
            values[min_val] = temp



def calculate_area(rectangle):
    x1 = rectangle.getP1().getX()
    x2 = rectangle.getP2().getX()
    y1 = rectangle.getP1().getY()
    y2 = rectangle.getP2().getY()
    length = x1 - x2
    width = y1 - y2
    return abs(length) * abs(width)


def rect_sort(rectangles):
    for i in range(len(rectangles)):
        min_val = rectangles[i]

        for j in range(i, len(rectangles)):
            rect_index = rectangles[j]
            area1 = calculate_area(min_val)
            area2 = calculate_area(rect_index)

            if area2 < area1:
                min_val = rectangles[j]

        if min_val != i:
            temp = rectangles[i]
            rectangles[i] = rectangles[min_val]
            rectangles[min_val] = temp




def trade_alert(filename):
    open_file = open(filename, "r")
    read_file = open_file.read()
    data = read_file.split(" ")
    for i in range(len(data)):
        if int(data[i]) > 830:
            print("ALERT VOLUME EXCEEDS AT".format(i + 1))
        elif int(data[i]) == 500:
            print("pay attention".format(i + 1))

    open_file.close()


def main():
    list1 = [1, 4, 3, 17, 22, 21]
    print(list1)
    selection_sort(list1)
    print(list1)
    trade_alert("trades.txt")
main()