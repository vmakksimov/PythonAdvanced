first = int(input())
second = int(input())
third = int(input())

def multiplication(one, two ,three):
    result = None
    if one > 0:
        result = 'positive'
    if two > 0:
        result = 'positive'
    if three > 0:
        result = 'positive'
    if one < 0:
        result = 'negative'
    if two < 0:
        result = 'negative'
    if three < 0:
        result = 'negative'
    if one == 0:
        result = 'zero'
    if two == 0:
        result = 'zero'
    if three == 0:
        result = 'zero'
    return result


call = multiplication(first, second, third)
print(call)