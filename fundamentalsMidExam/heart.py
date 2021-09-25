neightboorhood = [int(el) for el in input().split('@')]
command = input()
index_counter = 0
while not command == 'Love!':
    token = command.split()
    index = int(token[1])
    index_counter += index
    if index_counter > len(neightboorhood) - 1:
        index_counter = 0
    if neightboorhood[index_counter] == 0:
        print(f'Place {index_counter} already had Valentine\'s day.')
    else:
        neightboorhood[index_counter] -= 2
        if neightboorhood[index_counter] == 0:
            print(f'Place {index_counter} has Valentine\'s day.')
    command = input()
print(f'Cupid\'s last position was {index_counter}.')
house_left = 0
for house in neightboorhood:
    if house > 0:
        house_left += 1

if sum(neightboorhood) == 0:
    print(f'Mission was successful.')
else:
    print(f'Cupid has failed {house_left} places.')

