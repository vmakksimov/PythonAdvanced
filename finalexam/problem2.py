import re
number = int(input())
password = ''
for i in range(number):
    data = input()
    regex = r'(?P<group1>.{1,})(?P<start_sign>>)(?P<numbers>[0-9]{3})\|(?P<lower>[a-z]{3})\|(?P<higher>[A-Z]{3})\|(?P<symbols>[^<>]{3})(?P<end_sign><)\1'
    pattern = re.findall(regex, data)
    if pattern:
        for x in re.finditer(regex, data):
            h = x.group(3)
            k = x.group(4)
            o = x.group(5)
            l = x.group(6)
            password = 'Password: ' + h + k + o + l
            print(password)
            password = ''
    else:
        print(f'Try another password!')
