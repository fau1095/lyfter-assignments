

def check_amount_of_upper_cases(string):
    upper_cases = 0
    for char in string:
        if char.isupper():
            upper_cases += 1
    return upper_cases

def check_amount_of_lower_cases(string):
    lower_cases = 0
    for char in string:
        if char.islower():
            lower_cases += 1
    return lower_cases

if __name__ == '__main__':
    string = input("Enter a string: ")
    print(f'The amount of upper cases in the string is: {check_amount_of_upper_cases(string)}')
    print(f'The amount of lower cases in the string is: {check_amount_of_lower_cases(string)}')