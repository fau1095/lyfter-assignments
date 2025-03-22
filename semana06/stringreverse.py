#create a script to reverse a string

def reverse_string(string):
    return string[::-1]


if __name__ == '__main__':
    string = input("Enter a string: ")
    print(reverse_string(string))