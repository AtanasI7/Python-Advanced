number_of_students = int(input())
grades = {}


for _ in range(number_of_students):
    student_info = input().split(' ')
    name, grade = student_info
    grade = float(grade)

    if name not in grades:
        grades[name] = []

    grades[name].append(grade)

for key, value in grades.items():
    avg_grades = sum(value) / len(value)
    formatted = f"{' '.join([f'{x:.2f}' for x in value])}"
    print(f"{key} -> {formatted} (avg: {avg_grades:.2f})")
