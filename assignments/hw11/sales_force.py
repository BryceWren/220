from sales_person import SalesPerson
class SalesForce:
    def __init__(self):
        self.sales_people = []

    def add_data(self, file_name):
        file = open(file_name, "r")
        read_file = file.readline()
        for line in read_file.split(","):
            id = line[0]
            name = line[1]
            temp_person = SalesPerson(id, name)
            sales = line[2].split()
            temp_person.enter_sale(sales)
            self.sales_people.append(temp_person)

    def quota_report(self, quota):
        my_list = []
        for i in self.sales_people:
            id = i.get_id
            name = i.get_name
            total_sales = i.total_sales
            quota_met = i.met_quota(quota)
            whole_list = [id, name, total_sales, quota_met]
            my_list.append(whole_list)

    def top_seller(self):
        my_list = []
        for emp in range(len(self.sales_people) - 1):
            other = self.sales_people[emp + 1]
            best_emp = self.sales_people[emp].compare_to(other)
            if best_emp == 1:
                best_emp = emp
            my_list.append(best_emp)
            if best_emp < 0:
                best_emp = best_emp
            if best_emp == 0:
                my_list.append(best_emp + other)

    def individual_sales(self, employee_id):
        for emp in self.sales_people:
            id_in_person = emp[0]
            if employee_id == id_in_person:
                return emp
            else:
                return None

    def get_sale_frequencies(self):
        # {total:frequency}
        my_diction = {}
        for emp in self.sales_people:
            if emp[2] in my_diction:
                my_diction[emp[2]] = my_diction[emp[2]] + 1
            else:
                my_diction[emp[2]] = 1
