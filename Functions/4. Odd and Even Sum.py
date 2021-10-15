number = int(input())
number_as_string = str(number)
def even_odd(number):
    even_sum = []
    odd_sum = []

    for digit in number_as_string:
        if int(digit) % 2 == 0:
            even_sum.append(int(digit))

        elif int(digit) % 2 != 0:
            odd_sum.append(int(digit))

    print(f'Odd sum = {sum(odd_sum)}, Even sum = {sum(even_sum)}')
even_odd(number)