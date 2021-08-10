print('Day 24: Reading character by character from a file')

print("------------Reading 1 Char------------")
file = open('test1.txt', 'r')
while True:
    char = file.read(1)
    if not char:
        break
    print(char)
file.close()

print("------------Reading 6 Char------------")
with open('test1.txt', 'r') as file:
    while True:
        cha = file.read(6)
        if not cha:
            break
        print(cha)