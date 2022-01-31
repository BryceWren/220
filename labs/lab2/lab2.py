import math
def average():
    values = eval(input("Enter the values to be entered:"))
    rms = 0
    har_mean_a = 0 # accumulator
    geo_mean_a = 1
    for i in range(values):
        num = eval(input("Enter number:"))
        rms = rms + num**2
        har_mean_a = har_mean_a + 1/num
        geo_mean_a = geo_mean_a * num
    final_value = math.sqrt(rms / values)
    har_mean_b = values / (har_mean_a)
    geo_mean_b = geo_mean_a**(1/values)
    print("the rms mean is:", final_value)
    print("the harmonic mean is:", har_mean_b)
    print("the geometric mean is:", geo_mean_b)

