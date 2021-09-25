import math
count = 0
first_symbol_position = 0
result_first = 0
positions = 0
def position(counter, positions):
    for lett in ascii_uppercase:
        counter += 1
        if lett == first_letter:
            positions = counter
            counter = 0
            break
    return positions

def position2(counter, positions):
    for lett in ascii_uppercase:
        counter += 1
        if lett.lower() == last_letter:
            positions = counter
            counter = 0
            break
    return positions

string = input().split()
ascii_uppercase = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
last_symbol_position = 0
digits = ''
final_result = []
for el in string:
    first_letter = el[0]
    last_letter = el[-1]
    number = int(el[1:-1])
    if first_letter.isupper():
        positions = position(count, positions)
        result_first += (number / positions)

    elif first_letter.islower():
        positions = position(count, positions)
        result_first += number * positions

    if last_letter.isupper():
        positions = position2(count, positions)
        result_first -= last_symbol_position

    elif last_letter.islower():
        positions = position2(count, positions)
        result_first += last_symbol_position
    final_result.append(result_first)
    result_first = 0
print(f'{sum(final_result):.2f}')




