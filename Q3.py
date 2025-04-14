class Employee:
    employee_count = 0  # Class variable

    def __init__(self, name, salary):
        self.name = name
        self.salary = salary
        Employee.employee_count += 1

    @classmethod
    def total_employees(cls):
        return cls.employee_count

# Example Usage
e1 = Employee("John", 50000)
e2 = Employee("Jane", 60000)

print(f"Total Employees: {Employee.total_employees()}")
