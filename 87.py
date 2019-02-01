checklist = ["Portugal", "Germany", "Spain"]
checklist = [i + "\n" for i in checklist]


with open ("./Files/countries-missing.txt", "r") as file:
        content = file.readlines()

updated_list = sorted(checklist + content)

with open("./Files/countries-missing_fixed.txt", "w") as file:
        for i in updated_list:
                file.write(i)