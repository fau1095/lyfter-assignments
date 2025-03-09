import csv

countries_list = [
    {
        'name': 'Brazil',
        'population': 213000000,
        'capital': 'Brasília'
    },
    {
        'name': 'Argentina',
        'population': 45000000,
        'capital': 'Buenos Aires'
    },
    {
        'name': 'Uruguay',
        'population': 3400000,
        'capital': 'Montevideo'
    }
]
country_headers = ('name', 'population', 'capital')
    
def write_csv_file(file_path, data, headers):
    with open(file_path, 'w', encoding='utf-8') as file:
        writer = csv.DictWriter(file, headers)
        writer.writeheader()
        writer.writerows(data)
        
write_csv_file('countries.csv', countries_list, country_headers)

def write_csv_file2(file_path, data, headers):
  with open(file_path, 'w', encoding='utf-8') as file:
    writer = csv.DictWriter(file, headers)
    writer.writeheader()
    writer.writerows(data)

write_csv_file('countries2.csv', countries_list, countries_list[0].keys())