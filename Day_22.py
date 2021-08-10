print('Day 22: Find out given year is leap year or not')

print("\n------------Approach 1------------")
def checkleap(num):
    return ((num%4 == 0) and (num%100 != 0)) or (num%400 == 0)

year = int(input("Enter the year: "))
if checkleap(year):
    print(f'{year} is a Leap Year')
else:
    print(f'{year} is not a Leap Year')

print("\n------------Approach 2------------")
import calendar
def checkleap(num):
    if calendar.isleap(num):
        return f'{year} is a Leap Year'
    return f'{year} is not a Leap Year'

year = int(input("Enter the year: "))
print(checkleap(year))