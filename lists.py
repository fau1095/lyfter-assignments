my_pets_list = ['dog', 'cat', 'fish', 'bird']

my_pets_list.append('rabbit')
print(my_pets_list)


milky_way = ['sun', 'mercury', 'venus', 'earth', 'mars', 'jupiter', 'saturn', 'uranus', 'neptune', 'pluto']


pluto_index = 0
for index, planet in enumerate(milky_way):
    if planet == 'pluto':
        print(index)
        pluto_index = index
        break

deleted_element = milky_way.pop(9)
print(milky_way)
print(f'Deleted Planet: {deleted_element}')