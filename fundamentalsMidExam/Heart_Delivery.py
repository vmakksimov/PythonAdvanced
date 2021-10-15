neighborhood = [int(el) for el in input().split('@')]
command = input()
current_house = 0
counter = 0
while not command == 'Love!':
    data = command.split()
    action = data[0]
    if action == 'Jump':
        jump_lenght = int(data[1])
        current_house += jump_lenght
        if current_house > len(neighborhood) - 1:
            current_house = 0
        if 0 < current_house <= len(neighborhood):
            if neighborhood[current_house] > 0:
                neighborhood[current_house] -= 2
                if neighborhood[current_house] == 0:
                    print(f'Place {current_house} has Valentine\'s day.')
            else:
                print(f'Place {current_house} already had Valentine\'s day.')
        elif current_house == 0:
            if neighborhood[current_house] > 0:
                neighborhood[current_house] -= 2
                if neighborhood[current_house] == 0:
                    print(f'Place {current_house} has Valentine\'s day.')
            else:
                print(f'Place {current_house} already had Valentine\'s day.')

    command = input()
for index, digit in enumerate(neighborhood):
    if digit > 0:
        counter += 1
print(f'Cupid\'s last position was {current_house}.')
if sum(neighborhood) == 0:
    print(f'Mission was successful.')
else:
    print(f'Cupid has failed {counter} places.')

