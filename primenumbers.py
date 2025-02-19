

def create_list_from_input(list_of_numbers):
    created_list = list_of_numbers.split(',')
    created_list = [int(num.strip()) for num in created_list]
    return created_list
    

def prime_number(number):
    if number < 2:
        return False
    for i in range(2, number):
        if number % i == 0:
            return False
    return True
    
def prime_numbers_list_creator(created_list):
    prime_numbers = [num for num in created_list if prime_number(num)]
    return prime_numbers    

if __name__ == '__main__':
    list_of_numbers = input("Enter a list of numbers separated by ',': ")
    created_list = create_list_from_input(list_of_numbers)
    prime_numbers = prime_numbers_list_creator(created_list)
    print("Prime numbers in the list: ", prime_numbers)