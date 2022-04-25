from algorithms import *


def trade_alert(filename):
    open_file = open(filename, "r")
    read_file = open_file.read()
    data = read_file.split(" ")
    for i in range(len(data)):
        if int(data[i]) > 830:
            print("ALERT VOLUME EXCEEDS AT {}".format(i + 1))
        elif int(data[i]) == 500:
            print("pay attention {}".format(i + 1))

    open_file.close()


def main():
    list1 = [1, 4, 3, 17, 22, 21]
    print(list1)
    selection_sort(list1)
    print(list1)
    trade_alert("trades.txt")
    rec_list = [Rectangle(Point(1, 3), Point(2, 7)), Rectangle(Point(2, 5), Point(6, 10))]
    print(rec_list)
    rect_sort(rec_list)
    print(rec_list)

main()