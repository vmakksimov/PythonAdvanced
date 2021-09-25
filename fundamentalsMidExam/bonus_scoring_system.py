import math
import sys
students = int(input())
lectures = int(input())
bonus = int(input())
max_attends = 0
max_bonus = 0

if lectures and students == 0:
    print(f'Max Bonus: 0.')
    print(f'The student has attended 0 lectures.')
else:
    for student in range(1, students + 1):
        count_of_attend_each_student = int(input())
        total_bonus = math.ceil(count_of_attend_each_student / lectures * (5 + bonus))
        if total_bonus > max_bonus:
            max_bonus = total_bonus
            max_attends = count_of_attend_each_student
print(f'Max Bonus: {max_bonus}.')
print(f'The student has attended {max_attends} lectures.')