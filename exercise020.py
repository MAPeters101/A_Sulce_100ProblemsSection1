d = {"a": 1, "b": 2, "c": 3}
total = d["a"] + d["b"] + d["c"]
print(total)

print("*"*20)
total=0
for key in d:
    total += d[key]
print(total)

print("*"*20)
total = sum(d.values())
print(total)

print("*"*20)
total=0
for key, item in d.items():
    total += item
print(total)