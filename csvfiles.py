import csv


def ask_user_for_amount_of_videogames_to_register():
    return int(input('Enter the amount of video games you want to register: '))
#ask the user for the videogames information
def ask_for_videogame_information():
    videogame_info = []
    for i in range(ask_user_for_amount_of_videogames_to_register()):
        videogame_info.append({
                'name': input('Enter the name of the video game: '),
                'gender': input('Enter the name of the gender: '),
                'classification': input('Enter the name of the classification: '),
                'publisher': input('Enter the name of the publisher: ')
            })
    return videogame_info    

videogame_headers = ('name', 'gender', 'classification','publisher')
videogame_info = ask_for_videogame_information()
    
#write the csv file with commas    
def write_csv_file(file_path, data, headers):
    
    with open(file_path, 'w', encoding='utf-8') as file:
        writer = csv.DictWriter(file, headers)
        writer.writeheader()
        writer.writerows(data)        
        

write_csv_file('files/games.csv', videogame_info, videogame_headers)

#write the csv file with tabs instead of commas
def write_csv_file_with_tabs(file_path, data, headers):
    with open(file_path + '_tab.csv', 'w', encoding='utf-8') as file:
        writer = csv.DictWriter(file, headers, delimiter='\t')
        writer.writeheader()
        writer.writerows(data)
write_csv_file_with_tabs('files/games', videogame_info, videogame_headers)        