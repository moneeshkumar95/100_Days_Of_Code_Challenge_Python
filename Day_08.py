#Day 8 : Find the largest number in a list

print("\n---------Approach 1---------")
lis1 = [57,14,83,73, 74, 55, 86]
print("Largest number is",max(lis1))

print("\n---------Approach 2---------")
lis2 = [27, 98, 96, 55, 86, 27, 49]
lis2.sort()
print("Largest number is",lis2[-1])

print("\n---------Approach 3---------")
lis3 = [10, 73,20, 4, 45, 79,14, 63]
maxi = lis3[0]
for i in lis3:
    if i > maxi:
        maxi = i
print("Largest number is",maxi)