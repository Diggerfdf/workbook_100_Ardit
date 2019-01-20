import json
from pprint import pprint

filename = './Files/company1.json'


with open(filename, 'r') as f:
    d = json.loads(f.read())

pprint(d)
