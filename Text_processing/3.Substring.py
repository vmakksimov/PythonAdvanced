remove_text = input()
whole_text = input()

while remove_text in whole_text:
    whole_text = whole_text.replace(remove_text, '')
print(whole_text)


