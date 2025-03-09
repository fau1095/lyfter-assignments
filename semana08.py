def read_file(file_path):
    #empty list that we will fill with the songs from the file
    songs = []
    with open(file_path) as file:
        for line in file.readlines():
            songs.append(line.strip())
            print(f'Song {line}')
            
            
    return songs            
songs = read_file('files/songs.txt')

def write_on_a_new_file(songs):
    with open('new_file.txt', 'w') as file:
        #write the lines in the new file
        songs.sort()
        for line in songs:
            file.write(line + '\n')
            
write_on_a_new_file(songs)