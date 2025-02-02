class Employee:
    def __init__(self, fname, lname):
        self.fname = fname
        self.lname = lname


class SalaryEmployee(Employee):
    def __init__(self, fname, lname, salary):
        super().__init__(fname, lname)
        self.salary = salary

    def calculate_paycheck(self):
        return self.salary / 12


class HourlyEmployee(Employee):
    def __init__(self, fname, lname, weekly_hours, rate_per_hour):
        super().__init__(fname, lname)
        self.weekly_hours = weekly_hours
        self.rate_per_hour = rate_per_hour

    def calculate_paycheck(self):
        return self.weekly_hours * self.rate_per_hour


class CommissionEmployee(SalaryEmployee):
    def __init__(self, fname, lname, salary, no_of_sales, com_rate):
        super().__init__(fname, lname, salary)
        self.no_of_sales = no_of_sales
        self.com_rate = com_rate

    def calculate_paycheck(self):
        salary = super().calculate_paycheck()
        total_commission = self.no_of_sales * self.com_rate

        return salary + total_commission
