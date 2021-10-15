integers = [int(el) for el in input().split()]
command = input()
current_target = 0
shot_targets = 0

while not command == 'End':
    index = int(command)
    if 0 <= index <= len(integers) -1:
        if not integers[index] == -1:
            current_target = integers[index]
            integers[index] = -1
            shot_targets += 1
            for data, digit in enumerate(integers):
                if digit == -1:
                    continue
                if digit > current_target:
                    digit -= current_target
                    integers[data] = digit
                elif digit <= current_target:
                    digit += current_target
                    integers[data] = digit
    command = input()
integers_as_string = [str(x) for x in integers]
print(f'Shot targets: {shot_targets} -> {" ".join(integers_as_string)}')