"""
Name: <Bryce WRen>
<functions>.py

Problem: <using functions to solve different problems>

Certification of Authenticity:
<include one of the following>
I certify that this assignment is entirely my own work.
"""


def number_words(in_file_name, out_file_name):
    input_file = open(in_file_name, 'r')
    hw_file = input_file.read().split()
    out_file = open(out_file_name, 'w')
    for i in range(0, len(hw_file)):
        num = "{} {}".format(i + 1, hw_file[i])
        print(num, file=out_file)
    out_file.close()
    input_file.close()

#number_words("tests/number_words_3_input.txt", "pad.txt")

def hourly_wages(in_file_name, out_file_name):
    employee_file = open(in_file_name, "r")
    read_emp_file = employee_file.readlines()
    output_employee_file = open(out_file_name, "w")
    for i in range(len(read_emp_file)):
        emp_file_split = read_emp_file[i].split()
        wage = emp_file_split[2]
        hrs_worked = emp_file_split[3]
        wage_plus_bonus = (float(wage) * float(hrs_worked)) + (1.65 * int(hrs_worked))
        emp_f_name = emp_file_split[0]
        emp_l_name = emp_file_split[1]
        final_employ_file = "{} {} {:.2f}".format(emp_f_name, emp_l_name, wage_plus_bonus)
        print(final_employ_file, file=output_employee_file)
    employee_file.close()
    output_employee_file.close()
#hourly_wages("tests/hourly_wages_1_input.txt", "pad.txt")

def calc_check_sum(isbn):
    user = isbn.split("-")
    user_join = "".join(user)
    zero = 0
    for number in range(len(user_join)):
        int_user = int(user_join[number])
        absolute_mod = (abs(number + 1 % -11))
        zero += int_user * absolute_mod
    print("{}".format(zero))
    return zero


def send_message(file_name, friend_name):
    file_open = open(file_name, "r")
    read_friend_file = file_open.readlines()
    friend_file_output = open(friend_name + ".txt", "w")
    for i in read_friend_file:
        print(i, end="", file=friend_file_output)
    friend_file_output.close()
    file_open.close()


#send_message("tests/send_message_1_input.txt", "bob")


from encryption import encode, encode_better

def send_safe_message(file_name, friend_name, key):
    file_open = open(file_name, "r")
    read_friend_file = file_open.readlines()
    friend_file_output = open(friend_name + ".txt", "w")
    for i in read_friend_file:
        print(encode(i, key), end="", file=friend_file_output)

#send_safe_message("tests/send_message_1_input.txt", "bob", "7")


def send_uncrackable_message(file_name, friend_name, pad_file_name):
    file_open = open(file_name, "r")
    read_friend_file = file_open.read()
    key_open_file = open(pad_file_name, "r")
    key_read = key_open_file.read()
    friend_file_output = open(friend_name + ".txt", "w")
    encode = encode_better(read_friend_file, key_read)
    print(encode, file=friend_file_output)

send_uncrackable_message("tests/send_message_10_input.txt", "bob", "pad.txt")

if __name__ == '__main__':
    pass
