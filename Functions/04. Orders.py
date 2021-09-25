
product = input()
number = float(input())

def total_price(product_s, numbers):
    if product == 'coffee':
        return number * 1.50
    elif product == 'water':
        return number * 1.00
    elif product == 'coke':
        return number * 1.40
    elif product == 'snacks':
        return number * 2.00


print(f'{total_price(product, number):.2f}')
