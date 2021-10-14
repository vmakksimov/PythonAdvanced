def concatenate(expression='', *args):
    for i in args:
        expression += i
    return expression



print(concatenate("Soft", "Uni", "Is", "Great", "!"))