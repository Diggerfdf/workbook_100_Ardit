import json

filename = './Files/company1.json'

with open(filename, 'r+') as file:
    d = json.loads(file.read())

    d["employees"].append({"firstName": "Albert", "lastName": "Bert"})
    file.seek(0)
    json.dump(d, file, indent=4, sort_keys=True)
    file.truncate()

# Truncate erases everything from
# the cursor stop until the end of the file