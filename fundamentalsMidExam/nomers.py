integers = [int(el) for el in input().split()]
integers.sort(reverse=True)
if len(integers) < 2:
    print('No')
else:
    average_value = round(sum(integers) / len(integers), 2)
    new = [num for num in integers if num > average_value]
    if len(new) == 0:
        print('No')
    else:
        print(*new[:5])


