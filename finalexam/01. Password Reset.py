text = input()
new_text = ''
command = input()

while not command == 'Done':
    act = command.split()
    if act[0] == 'TakeOdd':
        for index, sym in enumerate(text):
            if index % 2 != 0:
                new_text += sym
        text = new_text
        print(new_text)

    elif act[0] == 'Cut':
        given_index = int(act[1])
        given_lenght = int(act[2])
        new = given_index + given_lenght
        text = text[:given_index] + text[new:]
        print(text)

    elif act[0] == 'Substitute':
        given_substring = act[1]
        new_substring = act[2]
        if given_substring in text:
            text = text.replace(given_substring, new_substring)
            print(text)
        else:
            print(f'Nothing to replace!')

    command = input()
print(f'Your password is: {text}')