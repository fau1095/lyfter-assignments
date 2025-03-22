my_pets_list = ['dog', 'cat', 'fish', 'bird']

my_pets_list.append('rabbit')
print(my_pets_list)

for my_pets in my_pets_list:
    print(f'I have a {my_pets}')
    

milky_way = ['sun', 'mercury', 'venus', 'earth', 'mars', 'jupiter', 'saturn', 'uranus', 'neptune', 'pluto']


for planet in milky_way:
    if planet == 'earth':
        print('Earth is a planet')
    else:
        print(f'The planet is {planet}')


for index in range(0, len(milky_way)):
    planet = milky_way[index]
    print(f'Index: {index} - Planet: {milky_way[index]}')

pluto_index = 0
for index, planet in enumerate(milky_way):
    if planet == 'pluto':
        print(index)
        pluto_index = index
        break

deleted_element = milky_way.pop(9)
print(milky_way)
print(f'Deleted Planet: {deleted_element}')


my_string = 'Hello World'
print(my_string[0])

my_string2 = 'Hello World'
for char in my_string2:
    print(char)

colors = ['red', 'green', 'blue', 'yellow', 'purple']

for color in colors:
    print(color)
    if color == 'blue':
        break


counter = 0
 
while True:
    print(counter)
    if counter > 10:
        break
    counter += 1