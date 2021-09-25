import re

data = input()
bought_furniture = []
furnitures = {}
result = 0
while not data == 'Purchase':
    regex = r'(?<!\W\S)(>>)(?P<object>[a-zA-Z]+)(<<)(?P<price>\d+(\.)?\d+)!(?P<quantity>\d+(\.)?(\d+)?)\b'
    pattern = re.finditer(regex, data)
    for el in pattern:
        t = el.groupdict()
        bought_furniture.append(t['object'])
        price = 'total_price'
        total = float(t['price']) * float(t['quantity'])
        if sum(furnitures.values()) == 0:
            furnitures[price] = total
        else:
            furnitures[price] += total

    data = input()
print('Bought furniture:')
for y in bought_furniture:
    print(y)
for key, value in furnitures.items():
    result += value
print(f'Total money spend: {result:.2f}')
