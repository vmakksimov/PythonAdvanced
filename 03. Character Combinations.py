def toString(List):
    return ''.join(List)


def character_combination(a, l, r):
    if l==r:
        print(toString(a))
    else:
        for i in range(l, r + 1):
            a[l], a[i] = a[i], a[l]
            character_combination(a, l + 1, r)
            a[l], a[i] = a[i], a[l]




text = list(input())
long = len(text)
character_combination(text, 0, long-1)


