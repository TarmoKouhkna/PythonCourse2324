class Employee:
    def __init__(self, name, emp_id, salary):
        self.name = name
        self.emp_id = emp_id
        self.salary = salary

    def calculate_salary(self):
        return self.salary


class Manager(Employee):
    def __init__(self, name, emp_id, salary, bonus):
        super().__init__(name, emp_id, salary)
        self.bonus = bonus

    def calculate_salary(self):
        return super().calculate_salary() + self.bonus


class Executive(Employee):
    def __init__(self, name, emp_id, salary, stock_options):
        super().__init__(name, emp_id, salary)
        self.stock_options = stock_options

    def calculate_salary(self):
        return super().calculate_salary() + self.stock_options


# Example Usage
employee1 = Employee("John Doe", "E1001", 50000)
manager1 = Manager("Jane Smith", "M2001", 60000, 10000)
executive1 = Executive("Alice Johnson", "X3001", 80000, 20000)

print("Employee 1 Salary:", employee1.calculate_salary())
print("Manager 1 Salary:", manager1.calculate_salary())
print("Executive 1 Salary:", executive1.calculate_salary())
