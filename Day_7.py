#Day 7 : Check number or word is Palindrome or not
print("\n---------Approach 1---------")
def pal(word):
    if word == word[::-1]:
        return f"{word} is palindrome"
    return f"{word} is not palindrome"
print(pal(input("Enter a word: ")))

print("\n---------Approach 2---------")
n = int(input("Enter a number: "))
reverse = 0
num = n
while (n != 0):
    remainder = n%10
    reverse = (reverse * 10) + remainder
    n = int(n/10)
if (num == reverse):
    print(f"{num} is palindrome")
else:
    print(f"{num} is not palindrome")