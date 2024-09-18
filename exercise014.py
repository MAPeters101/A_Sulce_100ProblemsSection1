from typing import OrderedDict

a = ["1", 1, "1", 2]
new_list = list(set(a))
print(new_list)
print("*"*20)
new_list=list(OrderedDict.fromkeys(a))
print(new_list)
print("*"*20)
b = []
for i in a:
    if i not in b:
        b.append(i)
print(b)