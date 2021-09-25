first = input()
command = input()


def transform(one, second):
    result = None
    if one == 'int':
        result = int(second) * 2
    elif one == 'real':
        result = f'{float(second) * 1.5:.2f}'
    elif one == 'string':
        result = f'${second}$'
    return result


one_to_call = transform(first, command)
print(one_to_call)