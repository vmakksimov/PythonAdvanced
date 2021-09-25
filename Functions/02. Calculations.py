
oper = input()
first = int(input())
second = int(input())

def calculator(operator, num_1, num_2):
    if operator == 'multiply':
        return num_1 * num_2
    elif operator == 'divide':
        return num_1 // num_2
    elif operator == 'add':
        return num_1 + num_2
    elif operator == 'subtract':
        return num_1 - num_2


print(calculator(oper, first, second))
