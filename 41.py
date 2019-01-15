import string

path = './Files/ex_41.txt'

with open(path, 'w+') as file:
    for letter in string.ascii_lowercase:
        file.write(letter + "\n")