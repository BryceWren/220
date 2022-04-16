class SalesPerson:
    def __init__(self, employee_id, name):
        self.employee_id = int(employee_id)
        self.name = name
        self.sales = []

    def get_id(self):
        return self.employee_id

    def get_name(self):
        return self.name

    def set_name(self, name):
        self.name = name

    def enter_sale(self, sale):
        self.sales.append(float(sale))

    def total_sales(self):
        total = 0.0
        for i in self.sales:
            total += i
        return total

    def get_sales(self):
        return self.sales

    def met_quota(self, quota):
        if self.total_sales() >= quota:
            return True

    def compare_to(self, other):

        if self.total_sales() > other.total_sales():
            return 1
        elif self.total_sales() < other.total_sales():
            return -1
        elif self.total_sales() == other.total_sales():
            return 0

    def __str__(self):
        return "{} - {} : {}".format(self.get_id,
                                     self.get_name(),
                                     self.get_sales())
    # when you print an object this is what the string object returns
