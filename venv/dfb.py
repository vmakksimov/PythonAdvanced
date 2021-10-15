command = input()
sides = {}
new_sides = {}
while not command == 'Lumpawaroo':
    if '|' in command:
        force_side, force_user = command.split(' | ')
        if not force_user in sides and not force_side in sides:
            sides[force_side] = [force_user]
        elif not force_user in sides[force_side]:
            sides[force_side].append(force_user)
        elif force_user in sides:
            continue
    elif '->' in command:
        force_user, force_side = command.split(' -> ')
        is_new_user = True
        for key, value in sides.items():
            value.remove(force_user)
            sides[force_side].append(force_user)
            print(f'{force_user} joins the {force_side} side!')
            is_new_user = False
        if is_new_user:
            sides[force_side].append(force_user)
            print(f'{force_user} joins the {force_side} side!')



    command = input()

sorted_by_name = dict(sorted(sides.items(), key=lambda x: len(x[0]), reverse=False))
for key, value in sorted_by_name.items():
    if len(value) > 0:
        value = sorted(value)
        print(f'Side: {key}, Members: {len(value)}')
        for v in value:
            print(f'! {"".join(v)}')