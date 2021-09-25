cities_specifics = {}
while True:
    text = input()
    if text == 'Sail':
        break
    else:
        data = text.split('||')
        city = data[0]
        population = int(data[1])
        gold = int(data[2])
        value = [population, gold]
        if city in cities_specifics:
            cities_specifics[city][0] += population
            cities_specifics[city][1] += gold
        else:
            cities_specifics[city] = value

command = input()

while not command == 'End':
    commands = command.split('=>')
    act = commands[0]
    town = commands[1]
    if act == 'Plunder':
        people = int(commands[2])
        town_gold = int(commands[3])
        cities_specifics[town][0] -= people
        cities_specifics[town][1] -= town_gold
        print(f'{town} plundered! {town_gold} gold stolen, {people} citizens killed.')
        if cities_specifics[town][0] == 0 or cities_specifics[town][1] == 0:
            del cities_specifics[town]
            print(f'{town} has been wiped off the map!')

    elif act == 'Prosper':
        prosper_gold = int(commands[2])
        if prosper_gold < 0:
            print('Gold added cannot be a negative number!')
        else:
            cities_specifics[town][1] += prosper_gold
            print(f'{prosper_gold} gold added to the city treasury. {town} now has {cities_specifics[town][1]} gold.')

    command = input()
    
sorted_by_name = dict(sorted(cities_specifics.items(), key=lambda kvp: (-kvp[1][1], kvp[0])))
if len(cities_specifics) > 0:
    print(f'Ahoy, Captain! There are {len(cities_specifics)} wealthy settlements to go to:')
    for key, town_spec in sorted_by_name.items():
        print(f'{key} -> Population: {town_spec[0]} citizens, Gold: {town_spec[1]} kg')
else:
    print('Ahoy, Captain! All targets have been plundered and destroyed!')






