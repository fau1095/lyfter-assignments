import json

name = input("Enter Pokemon name: ")
type_ = input("Enter Pokemon type: ").split(',')
hp = int(input("Enter HP: "))
attack = int(input("Enter Attack: "))
defense = int(input("Enter Defense: "))
sp_attack = int(input("Enter Sp. Attack: "))
sp_defense = int(input("Enter Sp. Defense: "))
speed = int(input("Enter Speed: "))

new_pokemon = {
    "name": {
        "english": name
    },
    "type": type_,
    "base": {
        "HP": hp,
        "Attack": attack,
        "Defense": defense,
        "Sp. Attack": sp_attack,
        "Sp. Defense": sp_defense,
        "Speed": speed
    }
}
def read_json_file(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        return json.load(file)

def write_json_file(file_path, data):
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            existing_data = json.load(file)
            
        if not isinstance(existing_data, list):
            existing_data = [existing_data]
        existing_data.append(data)
        
        with open(file_path, 'w', encoding='utf-8') as file:
            json.dump(existing_data, file, indent=4)
            
    except (json.JSONDecoder, FileNotFoundError):
        with open(file_path, 'w', encoding='utf-8') as file:
            json.dump(data, file, indent=4)
                   
print (read_json_file('files/pokemon.json'))   
write_json_file('files/pokemon.json', new_pokemon)
print(read_json_file('files/pokemon.json'))

