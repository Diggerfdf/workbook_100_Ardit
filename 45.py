import string
import os

os.chdir('./Files/Alphabet/')

letters = string.ascii_lowercase

for letter in letters:
    with open(letter + '.txt','w+')as file:
        file.write(letter)

# To check and create directory you can use

"""
if not os.path.exists("Alphabet"):
    os.makedirs("Alphabet")
"""

# Then you could use the path inside the with open

"""
for letter in string.ascii_lowercase:
    with open("Alphabet/" + letter + ".txt", "w+")as file:
        file.write(letter + "\n")
"""
