

def check_password(password):
    digit_counter = 0
    is_valid = True
    if len(password) < 6 or len(password) > 10:
        is_valid = False
        print('Password must be between 6 and 10 characters')
    for el in password:
        if not el.isdigit() and not el.isalpha():
            is_valid = False
            print('Password must consist only of letters and digits')
            break
    for el in password:
        if el.isdigit():
            digit_counter += 1
    if digit_counter < 2:
        is_valid = False
        print('Password must have at least 2 digits')

    return is_valid


password = input()
is_valid = check_password(password)
if is_valid:
    print('Password is valid')