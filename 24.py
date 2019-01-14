d = {"a": list(range(1,11)), "b": list(range(11, 21)), "c": list(range(21, 31))}

print("b has value {}".format(d["b"]))
print("c has value {}".format(d["c"]))
print("a has value {}".format(d["a"]))

# Ardit Solution:

for key, value in d.items():
    print(key, " has value ", value)