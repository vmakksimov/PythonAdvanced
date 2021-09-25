import re
number_of_codes = int(input())
product_group = ''
for code in range(number_of_codes):
    data = input()
    regex = r'(?P<delimiter>@#{1,})(?P<name>[A-Z][A-Za-z0-9]{4,}[A-Z])(?P<new>@#{1,})'
    pattern = re.findall(regex, data)
    if pattern:
        for x in re.finditer(regex, data):
            t = x.groupdict()
            str = t['name']
            for el in str:
                if el.isdigit():
                    product_group += el
            if len(product_group) == 0:
                product_group = '00'
                print(f"Product group: {product_group}")
                product_group = ''
            else:
                print(f"Product group: {product_group}")
                product_group = ''
    else:
        print("Invalid barcode")
