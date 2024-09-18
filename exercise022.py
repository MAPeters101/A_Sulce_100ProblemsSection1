from pprint import pprint
d = {'a':[i for i in range(1,11)], 'b':[i for i in range(11,21)], 'c':[i for i in range(21,31)]}
pprint(d)
print("*"*20)

for index, char in enumerate(('a','b','c')):
    l = []
    for i in range(index*10+1, index*10+11):
        l.append(i)
    d[char] = l
pprint(d)
print("*"*20)

d = {'a':list(range(1,11)), 'b':list(range(11,21)), 'c':list(range(21,31))}
pprint(d)