from sales_person import SalesPerson
class SalesForce:
    def __init__(self):
        self.sales_people = []

    def add_data(self, file_name):
        file = open(file_name, "r")
        read_file = file.readline()
        for line in read_file:
            self.sales_people.append(line)

    def quota_report(self, quota):
        pass

    def top_seller(self):
        pass

    def individual_sales(self, employee_id):
        pass

    def get_sale_frequencies(self):
        pass

