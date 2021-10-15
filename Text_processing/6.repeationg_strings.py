text = input()
counter = 0
final_word = ''
last_element = ''
while len(text) > counter:
    for el in text:
        counter += 1
        if el != last_element:
            last_element = ''
            last_element += el
            final_word += el

        else:
            continue
print(final_word)