def weighted_average(in_file_name, out_file_name):
    file_open = open(in_file_name, "r")
    read_file = file_open.readlines()
    output_file = open(out_file_name, "w")

    for student in read_file:
        read_file_split = student.split(":")
        student_name = read_file_split[0]
        number_split = read_file_split[1]
        number_split = number_split.split()
        accumulator = 0
        weight_accumulator = 0
        # most of the time put the accumulator before all the math
        for number in range(0, len(number_split), 2):
            algorithm = int(number_split[number]) * int(number_split[number + 1])
            accumulator += algorithm
            weight = int(number_split[number])

            weight_accumulator += weight

        average = accumulator / 100
        if weight_accumulator == 100:
            print("{}'s average: {}".format(student_name, average), file=output_file)
        elif weight_accumulator > 100:
            print("{}'s average: Error: weight is greater than 100".format(student_name), file=output_file)
        elif weight_accumulator < 100:
            print("{}'s average:Error: weight is less than 100".format(student_name), file=output_file)




weighted_average("example file", "test output")