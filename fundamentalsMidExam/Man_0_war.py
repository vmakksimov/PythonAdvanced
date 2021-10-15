pirate_ship = [int(el) for el in input().split('>')]
war_ship = [int(el) for el in input().split('>')]
maximum_health_capacity = int(input())
data = input().split()
game_over = True
while not data[0] == 'Retire' and game_over:
    if data[0] == 'Fire':
        if 0 <= int(data[1]) <= len(war_ship) - 1:
            war_ship[int(data[1])] -= int(data[2])
            if war_ship[int(data[1])] <= 0:
                print(f'You won! The enemy ship has sunken.')
                game_over = False
                break
    elif data[0] == 'Defend':
        if 0 <= int(data[1]) <= len(pirate_ship) - 1 and 0 <= int(data[2]) <= len(pirate_ship) - 1:
            for i in range(int(data[1]), int(data[2]) + 1):
                pirate_ship[i] -= int(data[3])
                if pirate_ship[i] <= 0:
                    print(f'You lost! The pirate ship has sunken.')
                    game_over = False
                    break

    elif data[0] == 'Repair':
        if 0 <= int(data[1]) <= len(pirate_ship) - 1:
            pirate_ship[int(data[1])] += int(data[2])
            if pirate_ship[int(data[1])] > maximum_health_capacity:
                pirate_ship[int(data[1])] = maximum_health_capacity

    elif data[0] == 'Status':
        counter_cells = 0
        for cell in pirate_ship:
            if cell < int(maximum_health_capacity * 0.20):
                counter_cells += 1
        print(f'{counter_cells} sections need repair.')

    data = input().split()

if game_over:
    print(f'Pirate ship status: {sum(pirate_ship)}')
    print(f'Warship status: {sum(war_ship)}')
