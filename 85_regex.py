import regex as re

with open("./Files/countries-raw.txt", "r") as file:
    text = file.read()
    text.replace("Top of Page", " ")
    space_off = re.compile(r'\n\n')
    text.replace("\r", " 1")
    print(text)