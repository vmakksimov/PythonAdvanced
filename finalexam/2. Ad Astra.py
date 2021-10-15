import re

data = input()
total_calories = 0
fifo = []
regex = r'(?P<delimiter>#|\|)(?P<item>[a-zA-Z\s]+)\1(?P<date>\d{2}/\d{2}/\d{2})\1(?P<calories>\d+)\1'
for match in re.finditer(regex, data):
    fifo.append([match.group(2), match.group(3), match.group(4)])
    total_calories += int(match.group(4))

days_left = total_calories // 2000

print(f'You have food to last you for: {days_left} days!')
for values in fifo:
    print(f'Item: {values[0]}, Best before: {values[1]}, Nutrition: {values[2]}')