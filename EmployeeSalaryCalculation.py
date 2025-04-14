def calculate_salary(hours_worked, hourly_rate):
    return hours_worked * hourly_rate

# Example usage
salary = calculate_salary(40, 20)  # 40 hours at $20/hour
print(f"Total Salary: ${salary}")
def calculate_salary(hours_worked, hourly_rate, bonus=0):
    return (hours_worked * hourly_rate) + bonus

# Example usage
salary_with_bonus = calculate_salary(40, 20, 100)  # $100 bonus
print(f"Total Salary with Bonus: ${salary_with_bonus}")
def calculate_salary(hours_worked, hourly_rate, bonus=0):
    overtime_hours = max(0, hours_worked - 40)  # Hours above 40
    regular_hours = min(40, hours_worked)
    
    # Regular pay + Overtime pay (1.5x) + Bonus
    return (regular_hours * hourly_rate) + (overtime_hours * hourly_rate * 1.5) + bonus

# Example usage
salary = calculate_salary(45, 20, 100)  # 45 hours, $20/hour, $100 bonus
print(f"Total Salary with Overtime and Bonus: ${salary}")
class Employee:
    def __init__(self, name, hourly_rate):
        self.name = name
        self.hourly_rate = hourly_rate

    def calculate_salary(self, hours_worked, bonus=0):
        overtime_hours = max(0, hours_worked - 40)
        regular_hours = min(40, hours_worked)
        total_salary = (regular_hours * self.hourly_rate) + (overtime_hours * self.hourly_rate * 1.5) + bonus
        return total_salary

# Example usage
emp = Employee("Alice", 25)
print(f"{emp.name}'s Salary: ${emp.calculate_salary(45, 200)}")
