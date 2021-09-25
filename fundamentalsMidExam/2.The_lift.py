people_waiting = int(input())
available_cabins = [int(el) for el in input().split()]
max_number = 4
total_available_sits = 0

for num, digit in enumerate(available_cabins):
    available_sits = max_number - digit
    total_available_sits += available_sits

for index, current_people_wagon in enumerate(available_cabins):
    available_sits_per_wagon = max_number - current_people_wagon
    if available_sits_per_wagon > 0 and people_waiting >= max_number:
        available_cabins[index] += available_sits_per_wagon
        people_waiting -= available_sits_per_wagon
        total_available_sits -= available_sits_per_wagon
    elif available_sits_per_wagon > 0 and max_number > people_waiting > 0:
        available_cabins[index] += people_waiting
        people_waiting -= available_cabins[index]
        total_available_sits -= available_cabins[index]

available_cabins_str = [str(el) for el in available_cabins]
if people_waiting == 0 and total_available_sits > 0:
    print(f'The lift has empty spots!\n'
          f'{" ".join(available_cabins_str)}')
elif people_waiting > 0 and total_available_sits == 0:
    print(f'There isn\'t enough space! {people_waiting} people in a queue!\n'
          f'{" ".join(available_cabins_str)}')
else:
    print(f'{" ".join(available_cabins_str)}')