number = int(input())
founded = {}

for plants in range(number):
    data = input().split('<->')
    key = data[0]
    rarity = int(data[1])
    founded[key] = [rarity, []]

command = input()
while not command == 'Exhibition':
    command = command.split(': ')
    command_status = command[0]
    command_given = command[1]
    if 'Rate' in command_status:
        plant, rating = command_given.split(' - ')
        rating = int(rating)
        if plant in founded:
            founded[plant][1].append(rating)
        else:
            print('error')

    elif 'Update' in command_status:
        plant, new_rarity = command_given.split(' - ')
        new_rarity = int(new_rarity)
        if plant in founded:
            founded[plant][0] = new_rarity
        else:
            print('error')

    elif 'Reset' in command_status:
        plant = command_given
        if plant in founded:
            founded[plant][1].clear()
        else:
            print('error')

    else:
        print('error')

    command = input()

for m, l in founded.items():
    rare = founded[m][0]
    if l[1]:
        avg_rate = (sum(l[1]) / len(l[1]))
    else:
        avg_rate = 0
    founded[m][1] = avg_rate

sorted_by_name = dict(sorted(founded.items(), key=lambda x: (x[1], x[1], x[0]), reverse=True))
#sorted_by_name = dict(sorted(founded.items(), key=lambda kvp: (-kvp[1][0], -kvp[1][1])))
print('Plants for the exhibition:')
for k, value in sorted_by_name.items():
    print(f'- {k}; Rarity: {value[0]}; Rating: {value[1]:.2f}')