# Answer 1:

a = ["1", 1, "1", 2]
print(list(set(a)))

# Answer 2: If you need to preserve the list order.

from collections import OrderedDict

a = ["1", 1, "1", 2]
a = list(OrderedDict.fromkeys(a))
print(a)

# Answer 3: Keeping the order with a for loop.
# But could take a lot of time

a = ["1", 1, "1", 2]
b = []

for i  in a:
    if i not in b:
        b.append(i)

print(b)