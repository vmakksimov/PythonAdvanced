secret_message = input()
command = input()

while not command == 'Reveal':
    act = command.split(':|:')
    command_given = act[0]

    if command_given == 'InsertSpace':
        index = int(act[1])
        secret_message = secret_message[:index] + ' ' + secret_message[index:]
        print(secret_message)

    elif command_given == 'Reverse':
        substring = act[1]
        if substring in secret_message:
            secret_message = secret_message.replace(substring, '', 1)
            substring = substring[::-1]
            secret_message = secret_message + substring
            print(secret_message)
        else:
            print('error')

    elif command_given == 'ChangeAll':
        substring = act[1]
        replacement = act[2]
        if substring in secret_message:
            secret_message = secret_message.replace(substring, replacement)
            print(secret_message)

    command = input()

print(f'You have a new text message: {secret_message}')