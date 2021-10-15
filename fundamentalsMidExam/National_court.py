first_employee = int(input())
second_employee = int(input())
third_employee = int(input())
people = int(input())
handle_people_per_hour = first_employee + second_employee + third_employee
hours_counter = 0
for x in range(1, people +1):
    if people <= 0:
        break
    hours_counter += 1
    if x % 4 == 0:
        continue
    else:
        people -= handle_people_per_hour
print(f'Time needed: {hours_counter}h.')


