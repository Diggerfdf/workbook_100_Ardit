import string

path = './Files/ex_43.txt'

a = string.ascii_lowercase[0::2]
b = string.ascii_lowercase[1::2]

with open(path, 'w+') as file:
    for i, j in zip(a, b):
        file.write(i + j + "\n")
