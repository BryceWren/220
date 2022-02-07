"""
Name: Bryce Wren
Assignment: Lab 3
"""
def main():
    roads = eval(input("How many roads were surveyed"))
    vehical_accum = 0
    for i in range(1, roads + 1):
        print("How many days were road", i, "surveyed")
        days_surveyed = eval(input())
        num = 0
        for j in range(1, days_surveyed + 1):
            print("how many cars were traveled on day", j)
            traveled_day = eval(input())
            num = num + traveled_day
        road_average = num / days_surveyed
        print("Road", i,"average vehicles per day:", road_average)
        vehical_accum = vehical_accum + num
    print(" Total number of vehicles traveled on all roads:", vehical_accum)
    average_vehical = vehical_accum / roads
    print("average number of vehicles per road: ", average_vehical)

main()
