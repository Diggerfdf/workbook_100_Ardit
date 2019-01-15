import string

path = './Files/ex_44.txt'

letters = string.ascii_lowercase + " "

a = letters[0::3]
b = letters[1::3]
c = letters[2::3]

with open(path, 'w+') as file:
    for i, j, k in zip(a, b, c):
        file.write(i + j + k + "\n")
