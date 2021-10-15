values = [int(el) for el in input().split()]
command = input()
while not command == 'end':
    if command == 'decrease':
        values = [x - 1 for x in values]
    else:
        tokens = command.split()
        index_1 = int(tokens[1])
        index_2 = int(tokens[2])
        if tokens[0] == 'swap':
            values[index_1], values[index_2] = values[index_2], values[index_1]
        elif tokens[0] == 'multiply':
            result = values[index_1] * values[index_2]
            values[index_1] = result
    command = input()
print(*values, sep=', ')