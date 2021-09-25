
health = 100
bitcoins = 0
dungeon_rooms = input().split('|')
room_counter = 0


for x in dungeon_rooms:
    command, number = x.split()
    number = int(number)
    room_counter += 1
    if command == 'potion':
        if health < 100:
            diff = 100 - health
            if number > diff:
                health += diff
                print(f'You healed for {diff} hp.')
            else:
                health += number
                print(f'You healed for {number} hp.')
            print(f'Current health: {health} hp.')
    elif command == 'chest':
        print(f'You found {number} bitcoins.')
        bitcoins += number
    else:
        health -= number
        if health > 0:
            print(f'You slayed {command}.')
        else:
            print(f'You died! Killed by {command}.')
            print(f'Best room: {room_counter}')
            break

if room_counter == len(dungeon_rooms):
    print(f'You\'ve made it!\n'
          f'Bitcoins: {bitcoins}\n'
          f'Health: {health}')
