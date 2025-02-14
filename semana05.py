""" numbers = [int(input("Enter a number: ")) for _ in range(10)]
print("Numbers ingressed by the user:", numbers)
print("The highest number was:", max(numbers))


#Ejericio 2
my_list = [1,2,3,4,5,6,7,8,9,10]

for number in reversed(my_list):
    if number % 2 == 0:
        my_list.remove(number)

print(my_list)

#Ejercicios de diccionarios

#Ejercicio 1
hotel_info = {
    'name': 'Hotel California',
    'stars': 5,
    #rooms should be a list and each room should contain a number, a floor and a price
    'rooms': [
        {
            'number': 101,
            'floor': 1,
            'price': 200
        }
    ]
}

#Ejercicio 2
first_list = ['name', 'age', 'city']
second_list = ['fabrizio', 29, 'San Jose']
created_dictionary = zip(first_list, second_list)
print(dict(created_dictionary)) """

#ejericio 3
list_of_keys = ['access_level', 'age']
employee_dict = {'name': 'John', 'email': 'john@ecorp.com', 'access_level': 5, 'age': 28}

for key in list_of_keys:
    if key in employee_dict.keys():
        deleted_key_from_dict = employee_dict.pop(key)
print(employee_dict)        