number_of_cars = int(input())
cars_to_driven = {}
for cars in range(number_of_cars):
    car_specifics = input().split('|')
    car = car_specifics[0]
    mileage = int(car_specifics[1])
    current_fuel = int(car_specifics[2])
    key = car
    value = [mileage, current_fuel]
    cars_to_driven[key] = value

command = input()
while not command == 'Stop':
    command = command.split(' : ')
    act = command[0]
    car_to_driven = command[1]
    if act == 'Drive':
        miles, needed_fuel = int(command[2]), int(command[3])
        if cars_to_driven[car_to_driven][1] >= needed_fuel:
            cars_to_driven[car_to_driven][0] += miles
            cars_to_driven[car_to_driven][1] -= needed_fuel
            print(f'{car_to_driven} driven for {miles} kilometers. {needed_fuel} liters of fuel consumed.')
            if cars_to_driven[car_to_driven][0] >= 100000:
                del cars_to_driven[car_to_driven]
                print(f'Time to sell the {car_to_driven}!')
        else:
            print('Not enough fuel to make that ride')

    elif act == 'Refuel':
        fuel_to_fill = int(command[2])
        max_fill = 75
        needed_fill = max_fill - cars_to_driven[car_to_driven][1]
        if needed_fill > fuel_to_fill:
            needed_fill = fuel_to_fill
            cars_to_driven[car_to_driven][1] += needed_fill
        else:
            cars_to_driven[car_to_driven][1] += needed_fill

        print(f'{car_to_driven} refueled with {needed_fill} liters')

    elif act == 'Revert':
        kilometers = int(command[2])
        cars_to_driven[car_to_driven][0] -= kilometers
        if cars_to_driven[car_to_driven][0] < 10000:
            cars_to_driven[car_to_driven][0] = 10000
        else:
            print(f'{car_to_driven} mileage decreased by {kilometers} kilometers')

    command = input()
sorted_by_name = dict(sorted(cars_to_driven.items(), key=lambda kvp: (-kvp[1][0], kvp[0])))
for car_name, specifics in sorted_by_name.items():
    print(f'{car_name} -> Mileage: {specifics[0]} kms, Fuel in the tank: {specifics[1]} lt.')