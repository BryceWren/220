import math
def average():
    values = eval(input("Enter the values to be entered:"))
    sum = 0
    har_mean_a = 0 #accumulator
    geo_mean_a = 1
    for i in range(values):
        num = eval(input("Enter number:"))
        sum = sum + num**2
        har_mean_a = har_mean_a + 1/num
        geo_mean_a = (geo_mean_a * num)
    final_value = math.sqrt(sum / values)
    har_mean_b = values / (har_mean_a)
    geo_mean_b = (geo_mean_a)**1/values
    print(final_value, har_mean_b, geo_mean_b)


def har_mean():
    values = eval(input("Enter the values to be entered:"))
    sum = 0
    for i in range(values):
        num = eval(input("Enter number:"))
        sum = sum + 1/num
    mean = values / sum
    print(mean)
