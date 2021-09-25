username = input()

command = input()

while not command == 'Registration':
    commands = command.split()
    act = commands[0]
    if act == 'Letters':
        case_type = commands[1]
        if case_type == 'Lower':
            username = username.lower()
            print(username)
        elif case_type == 'Upper':
            username = username.upper()
            print(username)
    elif act == 'Reverse':
        start_index = int(commands[1])
        end_index = int(commands[2])
        if start_index in range(len(username)) and end_index in range(len(username)):
            substring = username[start_index:end_index + 1:]
            new_substring = substring[::-1]
            print(new_substring)

    elif act == 'Substring':
        sub_string = commands[1]
        if sub_string in username:
            username = username.replace(sub_string, '', 1)
            print(username)
        else:
            print(f'The username {username} doesn\'t contain {sub_string}.')

    elif act == 'Replace':
        char = commands[1]
        if char in username:
            username = username.replace(char, '-')
            print(username)

    elif act == 'IsValid':
        valid_char = commands[1]
        if valid_char in username:
            print('Valid username.')
        else:
            print(f'{valid_char} must be contained in your username.')

    command = input()