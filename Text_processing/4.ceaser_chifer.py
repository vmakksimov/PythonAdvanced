text = input()
current_ord = None
new_text = ''
for char in text:
    for symbol in char:
        current_ord = ord(symbol) + 3
        new_text += chr(current_ord)
print(new_text)
