def calculate(nums):
    positive = sum(filter(lambda x: x > 0, nums))
    negative = sum(filter(lambda x: x < 0, nums))
    print(negative)
    print(positive)
    if abs(negative) > positive:
        return 'The negatives are stronger than the positives'
    else:
        return 'The positives are stronger than the negatives'


numbers = [int(el) for el in input().split()]
print(calculate(numbers))


