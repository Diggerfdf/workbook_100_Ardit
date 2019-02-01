with open("./Files/countries-raw.txt", "r") as file:
    content = file.readlines()

content = [i.strip("\n") for i in content if "\n" in i]
content = [i for i in content if i != ""]
content = [i for i in content if i != "Top of Page"]
content = [i for i in content if len(i) != 1]

print(content)

with open("./Files/countries_clean.txt", "w") as file:
    for i in content:
        file.write(i + "\n")
