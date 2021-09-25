command = input()
all_parts = 0
final_price = 0
taxes = 0
while True:
    if command == 'special':
        break
    elif command == 'regular':
        break
    command = float(command)
    if command < 0:
        print('Invalid price!')
    else:
        all_parts += command
    command = input()

taxes += all_parts * 0.20
final_price = all_parts + taxes
if final_price == 0:
    print('Invalid order!')
else:
    if command == 'special':
        final_price -= final_price * 0.1
        print(f'Congratulations you\'ve just bought a new computer!\n'
              f'Price without taxes: {all_parts:.2f}$\n'
              f'Taxes: {taxes:.2f}$\n'
              f'-----------\n'
              f'Total price: {final_price:.2f}$')
    elif command == 'regular':
        print(f'Congratulations you\'ve just bought a new computer!\n'
              f'Price without taxes: {all_parts:.2f}$\n'
              f'Taxes: {taxes:.2f}$\n'
              f'-----------\n'
              f'Total price: {final_price:.2f}$')
