#from itertools import combinations
#[print(", ".join(el)) for el in list(combinations(input().split(', '), int(input())))]

def combinations(names, count, current_name=[]):

    if len(current_name) == count:
        print(', '.join(current_name))
        return

    for i in range(len(names)):
        current_name.append(names[i])
        combinations(names[i+1:], count, current_name)
        current_name.pop()





names = input().split(', ')
n = int(input())
combinations(names, n)