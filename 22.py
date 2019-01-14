dic = {
    "a": list(range(1, 11)),
    "b": list(range(11,21)),
    "c": list(range(21,31))
}

for key, value in dic.items():
    print(key,value)

# Ardit Solution

from pprint import pprint

d = {"a": list(range(1,11)), "b": list(range(11, 21)), "c": list(range(21, 31))}
pprint(d)