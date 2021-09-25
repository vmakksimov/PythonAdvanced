string = input()
count = int(input())

def counted_string(text, repeat):
    result = ''
    for i in range(1, count + 1):
        result += string
    return result

print(counted_string(string, count))