my_range = range(1, 21)
print([str(i) for i in my_range])
print("*" * 20)
# map applies a function to an iterable
print(map(str, my_range))
# convert a map object to a list
print(list(map(str, my_range)))