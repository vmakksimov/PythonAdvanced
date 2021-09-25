first_student = int(input())
second_student = int(input())
third_student = int(input())
students_waiting = int(input())

resolved_students_per_hour = first_student + second_student + third_student
hours_counter = 0
while students_waiting > 0:
    hours_counter += 1
    students_waiting -= resolved_students_per_hour
    if hours_counter % 4 == 0:
        hours_counter += 1
print(f'Time needed: {hours_counter}h.')

