from employee_class import Employee


class Company:
    def __init__(self):
        self.employees = []

    def add_employee(self, new_employee):
        self.employees.append(new_employee)

    def display_employees(self):
        print("Current Employees:")
        print("---")
        for employee in self.employees:
            print(employee.fname, employee.lname)
        print("----------------------")

    def pay_employees(self):
        print("Paying Employees:")
        print("---")

        for employee in self.employees:
            print("Pay Check for: ", employee.fname, employee.lname)
            print(f"Amount: ${employee.calculate_paycheck():,.2f}")
        print("----------------------")


def main():
    company = Company()

    employee_1 = Employee("Kathiravan", "K", 32000)
    employee_2 = Employee("Lakshmi", "J", 52000)
    employee_3 = Employee("Shivani", "S", 12000)

    company.add_employee(employee_1)
    company.add_employee(employee_2)
    company.add_employee(employee_3)

    company.display_employees()
    company.pay_employees()


main()
