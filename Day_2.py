#100 days of python coding challenge
#Day 2 : Finding the max of two number
num_1 = int(input("Enter the first number: "))
num_2 = int(input("Enter the second number: "))
print("\nResults of Method_1")
if num_1 < num_2:
    print(f"{num_2} is the maximum")
else:
    print(f"{num_1} is the maximum")

print("\nResults of Method_2")
def max_finder(a,b):
    if a > b:
        return f"{num_1} is the maximum"
    return f"{num_2} is the maximum"
print(max_finder(num_1,num_2))

print("\nResults of Method_3")
maximum = max(num_1,num_2)
print(f"{maximum} is the maximum")