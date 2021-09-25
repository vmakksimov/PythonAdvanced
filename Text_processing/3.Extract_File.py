text = input()
sym = "\\"
index = 0
index2 = 0
final_name = ''
extension = None
for symbol in text:
    if symbol == sym and sym not in text[index +1:]:
        name = text[index +1:]
        for _ in name:
            if _ == '.':
                extension = name[index2 +1:]
                break
            else:
                final_name += _

            index2 +=1
    index += 1
print(f'File name: {final_name}')
print(f'File extension: {extension}')