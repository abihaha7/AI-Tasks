class Student:
    university = "ABC University"  # Class variable

    def __init__(self, name, age):
        self.name = name
        self.age = age

    @classmethod
    def change_university(cls, new_name):
        cls.university = new_name

# Example Usage
s1 = Student("Alice", 20)
s2 = Student("Bob", 22)

Student.change_university("XYZ University")
print(s1.university, s2.university)  # Both will reflect the change
