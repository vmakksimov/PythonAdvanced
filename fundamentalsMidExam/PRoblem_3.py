command = input().split()
chat = []
while not command[0] == 'end':
    act = command.pop(0)
    if act == 'Chat':
        chat.append(command[0])
    elif act == 'Delete':
        if command[0] in chat:
            chat.remove(command[0])
    elif act == 'Edit':
        for index, name in enumerate(chat):
            if name == command[0]:
                chat[index] = command[1]
    elif act == 'Pin':
        for index, name in enumerate(chat):
            if name == command[0]:
                poped = chat.pop(index)
                chat.append(poped)

    elif act == 'Spam':
        for el in command:
            chat.append(el)
    command = input().split()

for el in chat:
    print(f'{"".join(el)}')