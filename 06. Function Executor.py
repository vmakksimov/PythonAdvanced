


def multiply_numbers(num1, num2):
    return num1 * num2



def sum_numbers(num1, num2):
    return num1 + num2



def func_executor(*args):
    final_result = []
    for func, data in args:
        result = func(*data)
        final_result.append(result)
    return final_result


print(func_executor((sum_numbers, (1, 2)), (multiply_numbers, (2, 4))))