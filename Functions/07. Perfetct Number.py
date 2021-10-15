
def perfect_number(number):
    perfect_number = 0
    for x in range(1, number):
        if number % x == 0:
            perfect_number += x

    if perfect_number % number == 0:
        return True
    return False

number = int(input())
if perfect_number(number):
    print('We have a perfect number!')
else:
    print('It\'s not so perfect.')