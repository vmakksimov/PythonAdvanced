groceries = input().split('!')

command = input()
while not command == 'Go Shopping!':
    token = command.split()
    if token[0] == 'Urgent':
        if token[1] not in groceries:
            groceries.insert(0, token[1])
    elif token[0] == 'Unnecessary':
        if token[1] in groceries:
            groceries.remove(token[1])
    elif token[0] == 'Rearrange':
        if token[1] in groceries:
            groceries.remove(token[1])
            groceries.append(token[1])
    elif token[0] == 'Correct':
        if token[1] in groceries:
            index_old = groceries.index(token[1])
            groceries.remove(token[1])
            groceries.insert(index_old, token[2])
    command = input()
result = ', '.join(groceries)
print(result)