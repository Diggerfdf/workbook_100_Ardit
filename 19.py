d = {"a": 1, "b": 2}

d.update({"c": 3})

print(d)

# The above solution is good for numbers but,
# could cause problemas with a pair with spaces like name surname

d = {"a": 1, "b": 2}
d["c"] = 3
print(d)