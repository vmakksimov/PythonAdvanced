gifts_to_buy = input().split()
command = input()

while not command == 'No Money':
    data = command.split()
    if data[0] == 'OutOfStock':
        if data[1] in gifts_to_buy:
            for index, el in enumerate(gifts_to_buy):
                if el == data[1]:
                    gifts_to_buy[index] = 'None'

    elif data[0] == 'Required':
        if 0 <= int(data[2]) <= len(gifts_to_buy) -1:
            gifts_to_buy[int(data[2])] = data[1]

    elif data[0] == 'JustInCase':
        gifts_to_buy[-1] = data[1]

    command = input()
for gifts in gifts_to_buy:
    if gifts == 'None':
        continue
    else:
        print(f'{gifts}', end=' ')
