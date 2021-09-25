stops = input()

command = input()

while not command == 'Travel':
    command = command.split(':')

    if 'Add Stop' in command:
        index_str = int(command[1])
        string = command[2]
        if 0 <= index_str <= len(stops):
            stops = stops[:index_str] + string + stops[index_str:]
        print(stops)

    elif 'Remove Stop' in command:
        start_index = int(command[1])
        end_index = int(command[2])
        if start_index in range(len(stops)) and end_index in range(len(stops)):
            stops = stops[:start_index] + stops[end_index+1:]
        print(stops)

    elif 'Switch' in command:
        old_string = command[1]
        new_string = command[2]
        if old_string in stops:
            stops = stops.replace(old_string, new_string)
        print(stops)

    command = input()
print(f'Ready for world tour! Planned stops: {stops}')