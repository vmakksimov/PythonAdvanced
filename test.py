def print_nums(age, *args):
    return args

nums = print_nums(1, 2, 3, 4, age=25)

print(nums)