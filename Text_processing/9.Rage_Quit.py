text = input()
index = 0
string_name = ''
final_string = ''
while index < len(text):
    if not text[index].isdigit():
        string_name += text[index].upper()
        index += 1
    else:
        number = ''
        while index < len(text) and text[index].isdigit():
            number += text[index]
            index += 1
        number = int(number)
        string_name = string_name * int(number)
        final_string += string_name
        string_name = ''

unique = set(final_string)
print(f'Unique symbols used: {len(unique)}')
print(f'{final_string}')
