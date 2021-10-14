def check(nums, act):
    odd = sum(filter(lambda x: x % 2 != 0, nums))
    even = sum(filter(lambda x: x % 2 == 0, nums))
    if act == 'Odd':
        return odd * len(nums)
    else:
        return even * len(nums)

command = input()
numbers = [int(el) for el in input().split()]

print(check(numbers, command))

