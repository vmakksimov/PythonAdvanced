first_number = int(input())
second_number = int(input())
third_number = int(input())
result = 0

def add_and_subtract(first, second, third):
    result = (first_number + second_number) - third_number
    return result

print(add_and_subtract(first_number, second_number, third_number))
