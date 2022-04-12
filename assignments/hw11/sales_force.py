from sales_person import SalesPerson
class SalesForce:
    def __init__(self):
        self.sales_people = []

    def add_data(self, file_name):
        file = open(file_name, "r")
        read_file = file.readline()
        for line in read_file:
            individual_line = line.__str__()
            self.sales_people.append(individual_line)

    def quota_report(self, quota):
