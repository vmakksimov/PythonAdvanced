def index(list_of_numbers):
    index = int(len(list_of_numbers) / 2)
    list_of_numbers.insert(index, f'-{moves}a')
    list_of_numbers.insert(index, f'-{moves}a')
    return list_of_numbers

sequanse = input().split()
moves = 0
command = input()
while not command == 'end':
    index_1, index_2 = command.split()
    index_1 = int(index_1)
    index_2 = int(index_2)
    moves += 1
    if 0 <= index_1 < len(sequanse) and 0 <= index_2 < len(sequanse) and not index_1 == index_2:
        if sequanse[index_1] == sequanse[index_2]:
                removed = ''
                removed += sequanse[index_1]
                unwanted = [sequanse[index_1], sequanse[index_2]]
                for symbol in unwanted:
                    if symbol in sequanse:
                        sequanse.remove(symbol)
                print(f'Congrats! You have found matching elements - {removed}!')
        else:
            print('Try again!')

        if len(sequanse) == 0:
            print(f'You have won in {moves} turns!')
            break
    else:
        equal_to_check = index(sequanse)
        print(f'Invalid input! Adding additional elements to the board')

    command = input()
if len(sequanse) > 0:
    print(f'Sorry you lose :(\n'
          f'{" ".join(sequanse)}')