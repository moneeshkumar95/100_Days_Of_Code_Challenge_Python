#Day 12: Find the perfect number

print("\n---Perfect number or not---")
num = int(input("Enter a number: "))
perfect = 0
for i in range(1, num):
    if num%i == 0:
        perfect += i
if num == perfect:
    print( num,"is a Perfect number")
else:
    print(num, "is not a Perfect number")