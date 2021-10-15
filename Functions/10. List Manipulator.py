def exchange(nums_list, index):
    if command == 'end':
        return nums_list
    else:
        if 0 <= index < len(nums_list):

            first_part = nums_list[:index + 1]
            second_part = nums_list[index + 1:]
            exchange_list = second_part + first_part
            return exchange_list

        else:
            print('Invalid index')
            return nums_list

def get_max_odd_even(nums_list):
    filter_only_max_odds = []
    filter_only_max_even = []
    for el in nums_list:
        if command == 'max odd':
            if el % 2 == 1:
                filter_only_max_odds.append(el)
        else:
            if el % 2 == 0:
                filter_only_max_even.append(el)

    if filter_only_max_odds:
        max_odd = max(filter_only_max_odds)
        for index in range(len(nums_list) - 1, -1, -1):
            if nums_list[index] == max_odd:
                return index
    elif filter_only_max_even:
        max_even = max(filter_only_max_even)
        for index in range(len(nums_list) - 1, -1, -1):
            if nums_list[index] == max_even:
                return index
    else:
        return 'No matches'

def get_min_odd_even(nums_list):
    filter_only_min_odds = []
    filter_only_min_even = []
    for el in nums_list:
        if command == 'min odd':
            if el % 2 == 1:
                filter_only_min_odds.append(el)
        else:
            if el % 2 == 0:
                filter_only_min_even.append(el)

    if filter_only_min_odds:
        min_odd = min(filter_only_min_odds)
        for index in range(len(nums_list) - 1, -1, -1):
            if nums_list[index] == min_odd:
                return index
    elif filter_only_min_even:
        min_even = min(filter_only_min_even)
        for index in range(len(nums_list) - 1, -1, -1):
            if nums_list[index] == min_even:
                return index
    else:
        return 'No matches'

def first(nums_list):
    odd_el = []
    even_el = []
    count_break = 0
    if value > len(nums_list):
        return 'Invalid count'
    else:
        for nums in nums_list:
            if data == 'even':
                if nums % 2 == 0:
                    even_el.append(nums)
                    count_break += 1
                    if count_break == value:
                        return even_el
            else:
                if nums % 2 == 1:
                    odd_el.append(nums)
                    count_break += 1
                    if count_break == value:
                        return odd_el
    if sum(odd_el) > 0:
        return odd_el
    elif sum(even_el) > 0:
        return even_el
    elif sum(even_el) == 0:
        return even_el
    elif sum(odd_el) == 0:
        return odd_el
def last(nums_list):
    odd_el = []
    even_el = []
    count_break = 0
    if value > len(nums_list):
        return 'Invalid count'
    else:
        for nums in nums_list:
            if data == 'even':
                if nums % 2 == 0:
                    even_el.append(nums)
                    count_break += 1
                    if count_break == value:
                        return even_el
            else:
                if nums % 2 == 1:
                    odd_el.append(nums)
                    count_break += 1
                    if count_break == value:
                        return odd_el
    if sum(odd_el) > 0:
        return odd_el
    elif sum(even_el) > 0:
        return even_el
    elif sum(even_el) == 0:
        return even_el
    elif sum(odd_el) == 0:
        return odd_el
numbers_string = input().split()


numbers = list(map(int, numbers_string))

command = input()
while command != 'end':
    if command.split()[0] == 'exchange':
        index = int(command.split()[1])
        numbers = exchange(numbers, index)
    elif command.split()[0] == 'max':
        if command.split()[1] == 'odd':
            print(get_max_odd_even(numbers))
        elif command.split()[1] == 'even':
           print(get_max_odd_even(numbers))
    elif command.split()[0] == 'min':
        if command.split()[1] == 'even':
            print(get_min_odd_even(numbers))
        elif command.split()[1] == 'odd':
            print(get_min_odd_even(numbers))
    else:
            comman, value, data = command.split(' ')
            value = int(value)
            if comman == 'first':
                if data == 'odd':
                    print(first(numbers))
                else:
                    print(first(numbers))
            elif comman == 'last':
                if data == 'odd':
                    print(last(numbers))
                else:
                    print(last(numbers))
    command = input()
print(exchange(numbers, index))

