secret_message = input()
data = input()

while not data == 'Decode':
    command = data.split('|')
    act = command.pop(0)
    if act == 'Move':
        number = int(command[0])
        secret_message = secret_message[number:] + secret_message[:number]

    elif act == 'Insert':
        index_string = int(command[0])
        value_string = command[1]
        secret_message = secret_message[:index_string] + value_string + secret_message[index_string:]

    elif act == 'ChangeAll':
        old_string = command[0]
        new_string = command[1]
        secret_message = secret_message.replace(old_string, new_string)

    data = input()
print(f'The decrypted message is: {"".join(secret_message)}')