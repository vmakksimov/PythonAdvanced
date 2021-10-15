text = input()
reverse_word = {}
while not text == 'end':
    reverse_word[text] = text[::-1]

    text = input()
for key, value in reverse_word.items():
    print(f'{key} = {value}')