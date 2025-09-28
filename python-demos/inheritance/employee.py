class Employee:
    def __init__(self, fname, lname):
        self.fname = fname
        self.lname = lname


class SalaryEmployee(Employee):
    def __init__(self, fname, lname, salary):
        super().__init__(fname, lname)
        self.salary = salary

    def calcuate_paycheck(self):
        return self.salary / 52
        # Assuming salary is annual, divide by 52 weeks


class HourlyEmployee(Employee):
    def __init__(self, fname, lname, hourly_wage, hours_worked):
        super().__init__(fname, lname)
        self.hourly_wage = hourly_wage
        self.hours_worked = hours_worked

    def calcuate_paycheck(self):
        return self.hourly_wage * self.hours_worked


class CommissionEmployee(SalaryEmployee):
    def __init__(self, fname, lname, salary, salses_num, com_rate):
        super().__init__(fname, lname, salary)
        self.sales = salses_num
        self.commission_rate = com_rate

    def calcuate_paycheck(self):
        return super().calcuate_paycheck() + (self.commission_rate * self.sales)
