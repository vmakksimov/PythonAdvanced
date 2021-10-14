def math_operations(*args, **kwargs):
    operations = [int(x) for x in args]
    should_restart = True

    while should_restart:
        should_restart = False

        for index in range(len(operations)):
            if index == 0:
                kwargs['a'] += operations[index]

            elif index == 1:
                kwargs['s'] -= operations[index]

            elif index == 2:
                if operations[index] == 0:
                    continue
                else:
                    kwargs['d'] /= operations[index]

            elif index == 3:
                kwargs['m'] *= operations[index]

            if index == 4:
                operations = operations[4:]
                should_restart = True
                break

    return kwargs

print(math_operations(6, a=0, s=0, d=0, m=0))