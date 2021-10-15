first_number = int(input())
second_number = int(input())
def factorial(n):
    factorial_first = 1
    for x in range(n, 0, - 1):
        factorial_first *= x
    return factorial_first


factorial_number_first = factorial(first_number)
factorial_number_second = factorial(second_number)
result = factorial_number_first / factorial_number_second
print(f'{result:.2f}')




