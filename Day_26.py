print('Day 26: Converting python into JSON & Viceversa')

print("\n------------Python to JSON------------")
import json

dictionary = {"id": 1, "name": "Moneesh", "address": "Chennai"}

json_obj = json.dumps(dictionary, indent=2)
print(json_obj)
print(type(json_obj))

print("\n------------JSON to Python------------")
employee = '{"id": 1, "name": "Moneesh", "address": "Chennai"}'

employee_dict = json.loads(employee)

print(employee_dict)
print(type(employee_dict))