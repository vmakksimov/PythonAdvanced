import re

text = input()
cool_treshold = 1
cool_words = []
emoji_counter = 0
regex = r'(?P<delimiter>\:{2}|\*{2})(?P<name>[A-Z][a-z]{2,})\1'
for el in text:
    if el.isdigit():
        cool_treshold *= int(el)


for x in re.finditer(regex, text):
    full_word = x.group(0)
    first = x.group(2)
    result = 0
    emoji_counter += 1
    for character in first:
        result += ord(character)
    if result >= cool_treshold:
        cool_words.append(full_word)

print(f'Cool threshold: {cool_treshold}')
print(f'{emoji_counter} emojis found in the text. The cool ones are:')
for words in cool_words:
    print(f'{"".join(words)}')

