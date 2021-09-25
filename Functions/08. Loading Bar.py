
def loading_bar(bar_list, number_of_bars):
    for index in range(number_of_bars):
        bar_list[index] = '%'
    return bar_list

bar = []
for num in range(10):
    bar.append('.')

number = int(input())
remain = number // 10

filled = loading_bar(bar, remain)
if number > 0 and number < 100:
    print(f"{number}% [{''.join(filled)}]")
    print('Still loading...')
else:
    print(f'{number}% Complete!')
    print(f'[{"".join(filled)}]')