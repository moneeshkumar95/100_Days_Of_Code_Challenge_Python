#Day 14: Split and Join ans Slice a string

print("\n----------Split----------")
string1 = input("Enter a string line: ")
print(string1.split())

print("\n----------Join----------")
string2 = ['stay', 'home', 'and','stay', 'safe']
print(string2)
print(' '.join(string2))

print("\n----------Slice----------")
string3 = input("Enter a string line: ")
s2 = slice(len(string3)//2)
print(string3[s2])

