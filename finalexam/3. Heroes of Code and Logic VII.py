number_heroes = int(input())
best_heroes = {}
max_hp = 100
max_mp = 200
for heroes in range(number_heroes):
    data = input().split()
    hero = data[0]
    hp = int(data[1])
    mana = int(data[2])
    value = [hp, mana]
    best_heroes[hero] = value

command = input()

while not command == 'End':
    action = command.split(' - ')
    act = action[0]
    hero_name = action[1]
    amount = int(action[2])

    if act == 'CastSpell':
        spell_name = action[3]
        if int(best_heroes[hero_name][1]) >= amount:
            best_heroes[hero_name][1] -= amount
            print(f'{hero_name} has successfully cast {spell_name} and now has {best_heroes[hero_name][1]} MP!')
        else:
            print(f'{hero_name} does not have enough MP to cast {spell_name}!')

    elif act == 'TakeDamage':
        atacker = action[3]
        best_heroes[hero_name][0] -= amount
        if int(best_heroes[hero_name][0]) > 0:
            print(f'{hero_name} was hit for {amount} HP by {atacker} and now has {best_heroes[hero_name][0]} HP left!')
        else:
            del best_heroes[hero_name]
            print(f'{hero_name} has been killed by {atacker}!')

    elif act == 'Recharge':
        need_mana = max_mp - best_heroes[hero_name][1]
        if need_mana > amount:
            print(f"{hero_name} recharged for {amount} MP!")
            best_heroes[hero_name][1] += amount
        else:
            print(f"{hero_name} recharged for {need_mana} MP!")
            best_heroes[hero_name][1] += need_mana

    elif act == 'Heal':
        need_heal = max_hp - best_heroes[hero_name][0]
        if need_heal > amount:
            print(f"{hero_name} healed for {amount} HP!")
            best_heroes[hero_name][0] += amount
        else:
            print(f"{hero_name} healed for {need_heal} HP!")
            best_heroes[hero_name][0] += need_heal

    command = input()

sorted_by_name = dict(sorted(best_heroes.items(), key=lambda kvp: (-kvp[1][0], kvp[0])))
for name, power in sorted_by_name.items():
    print(f'{name}\n'
          f'HP: {power[0]}\n'
          f'MP: {power[1]}')
    #print(f'{name}')
    #print(f'HP: {power[0]}')
    #print(f'MP: {power[1]}')
