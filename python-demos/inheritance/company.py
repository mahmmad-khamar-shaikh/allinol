from employee import Employee, SalaryEmployee, HourlyEmployee, CommissionEmployee


class Company:
    def __init__(self):
        self.employees = []

    def add_employee(self, employee):
        self.employees.append(employee)

    def display_employees(self):
        for emp in self.employees:
            print(f"{emp.fname} {emp.lname}")

    def pay_employee(self):
        for emp in self.employees:
            paycheck = emp.calcuate_paycheck()
            print(f"Paying {emp.fname} {emp.lname}: ${paycheck:.2f}")


def main():
    company = Company()

    emp1 = SalaryEmployee("John", "Doe", 60000)
    emp2 = HourlyEmployee("Jane", "Smith", 20, 80)
    emp3 = CommissionEmployee("Alice", "Johnson", 50000, 20000, 0.10)

    company.add_employee(emp1)
    company.add_employee(emp2)
    company.add_employee(emp3)

    company.display_employees()
    company.pay_employee()


main()
