
import re

text = input()
check = []
counter_match = 0
counter_pairs = 0
regex = r'(?P<delimiter>#|@)(?P<first_name>[A-Za-z]{3,})\1\1(?P<second_name>[A-Za-z]{3,})\1'

for x in re.finditer(regex, text):
    r = x.groupdict()
    counter_pairs += 1
    if r['first_name'] == r['second_name'][::-1]:
        pair = r['first_name'] + ' <=> ' + r['second_name']
        check.append(pair)
        counter_match += 1

if counter_pairs > 0:
    print(f'{counter_pairs} word pairs found!')
    if counter_match > 0:
        print('The mirror words are:')
        print(*check, sep=', ')
    else:
        print('No mirror words!')
else:
    print("No word pairs found!")
    print("No mirror words!")


