specifics = {}

while True:
    command = input()
    if command == 'Results':
        break
    else:
        commands = command.split(':')
        act = commands[0]
        name = commands[1]
        if act == 'Add':
            health = int(commands[2])
            energy = int(commands[3])
            value = [health, energy]
            if name in specifics:
                specifics[name][0] += health
            else:
                specifics[name] = value

        elif act == 'Attack':
            attacker_name = name
            deffender_name = commands[2]
            damage = int(commands[3])
            if attacker_name in specifics and deffender_name in specifics:
                specifics[deffender_name][0] -= damage
                specifics[attacker_name][1] -= 1
                if specifics[deffender_name][0] <= 0:
                    del specifics[deffender_name]
                    print(f'{deffender_name} was disqualified!')
                if specifics[attacker_name][1] <= 0:
                    del specifics[attacker_name]
                    print(f'{attacker_name} was disqualified!')

        elif act == 'Delete':
            data = commands[1]
            if data == 'All':
                specifics.clear()
            else:
                if name in specifics:
                    del specifics[name]

sorted_by_name = dict(sorted(specifics.items(), key=lambda kvp: (-kvp[1][0], kvp[0])))
print(f'People count: {len(specifics)}')
for names, spec in sorted_by_name.items():
    print(f'{names} - {spec[0]} - {spec[1]}')
