checklist = ["Portugal", "Germany", "Munster", "Spain"]

with open("./Files/countries_clean.txt", "r") as file:
    content = file.readlines()

content = [i.strip("\n") for i in content if "\n" in i]
checked = [i for i in content if i in checklist]

print(checked)

