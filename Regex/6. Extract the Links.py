
import re
sites = []
data = input()
while data:
    regex = r'(^|(?<=\s))\bw{3}(\.)[a-zA-Z0-9-]+(\.[a-z]+)+($|(?=\s))'
    pattern = re.finditer(regex, data)

    for x in pattern:
        t = x.group(0).strip()
        print(t)
    data = input()


