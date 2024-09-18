d = {"a": 1, "b": 2, "c": 3}
e = {}
for key, value in d.items():
    if d[key] <= 1:
        e[key] = d[key]
print(e)
print("*"*20)

e={key:value for key,value in d.items() if d[key]<=1}
print(e)
print("*"*20)

e=dict((key,value) for key,value in d.items() if value<=1)
print(e)