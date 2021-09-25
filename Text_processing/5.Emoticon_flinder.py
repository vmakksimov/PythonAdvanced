text = input()
index = 0
emoticon = ''
for symbol in text:
    if symbol == ':':
        emoticon += text[index:index + 2]
        print(emoticon)
        emoticon = ''
    index += 1
