strings = input().split()
string1 = strings[0]
string2 = strings[1]
total_sum = 0
first_sting = []
second_digit = []

for chr in string1:
    first_sting.append(ord(chr))
for chr in string2:
    second_digit.append(ord(chr))
cycle_iterations = min(len(first_sting), len(second_digit))
max_cycle = max(len(first_sting), len(second_digit)) - cycle_iterations
if len(first_sting) != len(second_digit):
    if len(first_sting) > len(second_digit):
        for i in range(0, cycle_iterations):
            product = first_sting[i] * second_digit[i]
            total_sum += product

        for m in range(cycle_iterations, len(first_sting)):
            total_sum += first_sting[m]
    elif len(first_sting) < len(second_digit):
        for i in range(0, cycle_iterations):
            product = first_sting[i] * second_digit[i]
            total_sum += product
        for m in range(cycle_iterations, len(second_digit)):
            total_sum += second_digit[m]
else:
    for i in range(0, cycle_iterations):
        product = first_sting[i] * second_digit[i]
        total_sum += product


print(total_sum)
