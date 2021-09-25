number_of_pieces = int(input())
pieces = {}

for nums in range(number_of_pieces):
    songs = input().split('|')
    key = songs[0]
    value = [songs[1], songs[2]]
    pieces[key] = value
command = input()
while not command == 'Stop':
    command = command.split('|')
    act = command[0]
    piece = command[1]
    if act == 'Add':
        composer = command[2]
        note = command[3]
        if piece in pieces:
            print(f'{piece} is already in the collection!')
        else:
            pieces[piece] = [composer, note]
            print(f"{piece} by {composer} in {note} added to the collection!")

    elif act == 'Remove':
        if piece in pieces:
            removed = pieces.pop(piece)
            print(f'Successfully removed {piece}!')
        else:
            print(f'Invalid operation! {piece} does not exist in the collection.')

    elif act == 'ChangeKey':
        new_key = command[2]
        if piece in pieces:
            pieces[piece][1] = new_key
            print(f'Changed the key of {piece} to {new_key}!')
        else:
            print(f'Invalid operation! {piece} does not exist in the collection.')

    command = input()

sorted_by_name = dict(sorted(pieces.items(), key=lambda x: (x[0], x[0])))
for el, digit in sorted_by_name.items():
    print(f'{el} -> Composer: {digit[0]}, Key: {digit[1]}')