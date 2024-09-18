letters = "abcdefghijklmnopqrstuvwxyz"
for char in letters:
    print(char)

#print(chr(ord('a')))

print("*"*20)
for value in range(ord('a'), ord('z')+1):
    print(chr(value))

print("*"*20)
import string
for letter in string.ascii_lowercase:
    print(letter)