
import re
text = input()
travel_points = 0
destinations = []
regex = r'(?P<delimiter>=|\/)(?P<name>[\bA-Z][A-Za-z]{2,})\1'

for x in re.finditer(regex, text):
    destinations.append(x.group(2))
    travel_points += len(x.group(2))

print(f'Destinations: {", ".join(destinations)}')
print(f'Travel Points: {travel_points}')