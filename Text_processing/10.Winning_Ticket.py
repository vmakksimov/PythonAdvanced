tickets = input().split(',')
winning_symbols = '@#$^'
winning_el_left = ''
winning_el_right = ''
def halfs(l_half, r_half):
    winning_el = ''
    for el in l_half:
        if el in winning_symbols:
            winning_el += el
    return winning_el
for ticket in tickets:
    t = ticket.strip()
    if len(t) != 20:
        print('invalid ticket')
    elif len(t) == 20:
        left_half = t[:10]
        right_half = t[10:]
        halfs(left_half, right_half)

        print(f'ticket "{t}" - no match')
        for el in right_half:
            if el in winning_symbols:
                winning_el_right += el
            else:
                print(f'ticket "{t}" - no match')
        if winning_el_left == winning_el_right:
            print(f'ticket "{t}" - {len(winning_el_left)}{"".join(set(winning_el_left))}')


