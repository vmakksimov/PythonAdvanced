n = int(input())
plants = {}
for x in range(n):
    data = input().split("<->")
    plant_name = data[0]
    rarity = int(data[1])
    plants[plant_name] = {'rarity': rarity, 'ratings': []}

command = input()
while not command == "Exhibition":
    command_info = command.split(": ")
    name = command_info[0]
    command_params = command_info[1]
    if name == "Rate":
        plant_name, rating = command_params.split(" - ")
        rating = int(rating)
        if plant_name in plants:
            plants[plant_name]['ratings'].append(rating)
        else:
            print("error")
    elif name == "Update":
        plant_name, new_rarity = command_params.split(" - ")
        new_rarity = int(new_rarity)
        if plant_name in plants:
            plants[plant_name]['rarity'] = new_rarity
        else:
            print("error")
    elif name == "Reset":
        plant_name = command_params
        if plant_name in plants:
            plants[plant_name]['ratings'].clear()
        else:
            print("error")
    else:
        print("error")
    command = input()

for plant_name, value in plants.items():
    if value['ratings']:
        avg = sum(value['ratings']) / len(value['ratings'])
    else:
        avg = 0
    plants[plant_name]['avg'] = avg

sorted_plants = sorted(plants.items(), key=lambda kvp: (-kvp[1]['rarity'], -kvp[1]['avg']))
print("Plants for the exhibition:")

for plant_name, value in sorted_plants:
    print(f"- {plant_name}; Rarity: {value['rarity']}; Rating: {value['avg']:.2f}")