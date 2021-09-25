first_char = input()
second_char = input()

def between_char(first_char, second_char):
    for i in range(ord(first_char) + 1, ord(second_char)):
        print(chr(i), end=' ')

between_char(first_char, second_char)