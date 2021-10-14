def even_odd(*args):
    numbers = args[:-1]
    if 'even' in args:
        return list(filter(lambda x: x % 2 == 0, numbers))
    elif 'odd' in args:
        return list(filter(lambda x: x % 2 != 0, numbers))


print(even_odd(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, "odd"))