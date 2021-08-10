#Day 13: Which year will be your 100th birthday
from datetime import date
print("\n---100th Birthday Finder---")
name = input("Enter your name: ")
age = int(input("Enter your age: "))
current_year = date.today().year
if age <= 100:
    remaining_age = 100 - age
    hundred_year = current_year + remaining_age
    print( f'\n{age}-years old {name.capitalize()} will celebrate 100th birthday in {hundred_year}')
else:
    remaining_age = age - 100
    hundred_year = current_year - remaining_age
    print(f'n{age}-years old {name.capitalize()} already celebrated 100th birthday in {hundred_year}')