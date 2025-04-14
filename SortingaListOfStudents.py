students = [
    {"name": "Alice", "score": 85, "age": 17},
    {"name": "Bob", "score": 92, "age": 16},
    {"name": "Charlie", "score": 78, "age": 18},
    {"name": "David", "score": 92, "age": 17},
]

# Sort by score in descending order
sorted_by_score = sorted(students, key=lambda x: x["score"], reverse=True)

# Display sorted list
for student in sorted_by_score:
    print(student)
sorted_by_age = sorted(students, key=lambda x: x["age"])

for student in sorted_by_age:
    print(student)
sorted_by_score_then_age = sorted(students, key=lambda x: (-x["score"], x["age"]))

for student in sorted_by_score_then_age:
    print(student)
def sort_students(students, by="score", descending=True):
    reverse = descending  # True for descending, False for ascending
    return sorted(students, key=lambda x: x[by], reverse=reverse)

# Example: Sort by age in ascending order
sorted_students = sort_students(students, by="age", descending=False)
print(sorted_students)
