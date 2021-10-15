

def palidrome(palidorme):
    reversed_element = palidorme[::-1]
    if palidorme == reversed_element:
        return True
    return False

def separate_elements(text, sep):
    numbers_as_string = text.split(sep)
    return numbers_as_string

palindrome = input()
nums_string = separate_elements(palindrome, ', ')
for el in nums_string:
    print(palidrome(el))

