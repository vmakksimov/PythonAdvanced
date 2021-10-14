def final(box, symbols):
    if box > 0:
        return f"There is free space in the box. You could put {box} more cubes."
    else:
        result = 0
        for k in symbols:
            if not k == 'Finish':
                result += k
        return f'No more free space! You have {result} more cubes.'


def fill_the_box(*args):
    new_nums = []
    for el in args:
        new_nums.append(el)

    size = new_nums[:3]
    symbols_left = new_nums[3:]
    box_size = 1
    for index in size:
        box_size *= index
    for index in range(len(symbols_left)):
        if symbols_left[index] == 'Finish':
            return final(box_size, symbols_left)
        else:
            if symbols_left[index] < box_size:
                box_size -= symbols_left[index]
                symbols_left[index] = 0
            elif box_size < symbols_left[index]:
                symbols_left[index] -= box_size
                box_size = 0
                return final(box_size, symbols_left)
            elif box_size == symbols_left[index]:
                box_size = 0
                symbols_left[index] = 0
                return final(box_size, symbols_left)



print(fill_the_box(2, 8, 2, 2, 1, 7, 3, 1, 5, "Finish"))