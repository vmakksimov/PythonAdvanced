friends = input().split(', ')
command = input().split()
count_black = 0
blacklisted = []
lost_names = 0

while not command[0] == 'Report':
    act = command.pop(0)
    if act == 'Blacklist':
        if command[0] in friends:
            for index, name in enumerate(friends):
                if name == command[0]:
                    old_name = name
                    friends[index] = 'Blacklisted'
                    print(f'{old_name} was blacklisted.')
                    blacklisted.append(name)
                    count_black += 1
                    break
        elif command[0] not in friends:
            print(f'{command[0]} was not found.')

    elif act == 'Error':
        if 0 <= int(command[0]) <= len(friends) - 1 and friends[int(command[0])] != 'Blacklisted' and friends[int(command[0])] != 'Lost':
            lost_name = friends[int(command[0])]
            friends[int(command[0])] = 'Lost'
            print(f'{lost_name} was lost due to an error.')
            lost_names += 1
        else:
            continue

    elif act == 'Change':
        if 0 <= int(command[0]) <= len(friends) - 1:
            old_name = friends[int(command[0])]
            new_name = command[1]
            friends[int(command[0])] = new_name
            command[1] = old_name
            print(f'{old_name} changed his username to {new_name}.')
        else:
            continue

    command = input().split()

print(f'Blacklisted names: {count_black}')
print(f'Lost names: {lost_names}')
print(f'{" ".join(friends)}')

