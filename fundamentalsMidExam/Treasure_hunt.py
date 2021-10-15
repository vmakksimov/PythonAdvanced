loot = input().split('|')
found = False
data = input().split()

while not data[0] == 'Yohoho!':
    if data[0] == 'Loot':
        data.pop(0)
        for loots in data:
            if loots not in loot:
                loot.insert(0, loots)
    elif data[0] == 'Drop':
        if 0 <= int(data[1]) <= len(loot) - 1:
            poped_loot = loot.pop(int(data[1]))
            loot.append(poped_loot)
    elif data[0] == 'Steal':
        if int(data[1]) < len(loot):
            diff = len(loot) - int(data[1])
            stolen_items = loot[diff:]
            loot = loot[:diff]
            print(f'{", ".join(stolen_items)}')
        else:
            print(f'{", ".join(loot)}')
            print("Failed treasure hunt.")
            found = True
            break
    data = input().split()

if not found:
    lenght_count = 0
    for count in loot:
        lenght_count += len(count)
    print(f'Average treasure gain: {lenght_count / len(loot):.2f} pirate credits.')